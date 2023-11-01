from pydantic import BaseModel

class Model(BaseModel):
    id : int
    name : str
    password : str
    