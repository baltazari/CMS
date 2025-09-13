from pydantic import BaseModel, EmailStr, constr
from typing import Annotated

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: Annotated[str, constr(min_length=6)]
    pasword_repeat: str
    phone_number:str 
    
    
    def validate_password(self):
        if self.password != self.pasword_repeat:
            raise ValueError("passwords do not match")