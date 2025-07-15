# class Member:
#     def __init__(self, name, id, pw, addr):
#         self.name = name
#         self.id = id
#         self.pw = pw
#         self.addr = addr

# pip install pydantic

from pydantic import BaseModel, Field
class Member(BaseModel):
    name:str = Field(min_length=2, max_length=10, description='이름')
    id:int = Field(gt=0, lt=100, description='아이디')
    pw:str 
    addr:str = Field(default='서울', description='주소')

if __name__ == '__main__':
    member = Member(name='이재성', id=12, pw='1234', addr='서울시 서초구 대전동')
    print(member)