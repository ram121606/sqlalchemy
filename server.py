from fastapi import FastAPI
import uvicorn
from models.model import Model
from db.db import User
from db.db_con import engine
from db.db_con import session


app = FastAPI()

User.metadata.create_all(engine)

@app.get('/')
def home():
    return "Home"

@app.get('/get')
def get_items():
    items = session.query(User).all()
    return items

@app.post('/create')
def create(payload : Model ):
    user = User(name = payload.name, id = payload.id, password = payload.password)
    session.add(user)
    session.commit()
    session.refresh(user)


if __name__ == "__main__":
    uvicorn.run('server:app' , port=6969 , reload=True)