from fastapi import FastAPI , HTTPException
import uvicorn
from models.model import Model
from db.db import User
from db.db_con import engine,session


app = FastAPI()

User.metadata.create_all(engine)

@app.get('/')
def home():
    return "Home"


@app.get('/get')
def get_items():
    items = session.query(User).all()
    return items


@app.get('/get/{name}')
def get_name(name : str):
    res = session.query(User).filter(User.name == name).first()
    if(res != None):
        return res
    else:
        raise HTTPException(status_code=404 , detail='No such record exists')
    

@app.post('/create')
def create(payload : Model ):
    # user = User(name = payload.name, id = payload.id, password = payload.password)
    user = User(**payload.model_dump())
    res = session.query(User).filter(User.name == payload.name).first()
    if(res == None):
        session.add(user)
        session.commit()
    else:
        raise HTTPException(status_code=409 , detail='Already exists')
    

@app.delete('/delete/{id}')
def delete(id : int):
    res = session.query(User).get(id)
    if not res:
        raise HTTPException(status_code=404 , detail='Id not found')
    else:
        session.delete(res)
        session.commit()
        return "Deleted Successfully"
    
@app.put('/update')
def update(id: int , alternateName: str):
    res = session.query(User).get(id)
    if not res:
        raise HTTPException(status_code=404 , detail='Id not found')
    else:
        res.name = alternateName
        return "Updated Successfully"
    

if __name__ == "__main__":
    uvicorn.run('server:app' , port=6969 , reload=True)