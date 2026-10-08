from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'nitish'
    age : Optional[int] = None
    Email: EmailStr
    cgpa: float = Field(gt=0, lt = 10,default=5)


new_student= { 'name':'vinay' , 'age' : 24, 'Email' : 'emptyhands@example.com'  }

student= Student(**new_student)

print(dict(student))
print(type(student))
print(student.model_dump_json())

