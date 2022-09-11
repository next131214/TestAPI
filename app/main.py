from fastapi import FastAPI, Request, Depends ,HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials,OAuth2PasswordBearer
from lib.authentication import simple_authentication
from db import session
from model.table2 import Table2,Table2Table
from model.table1 import Table1,Table1Table



app = FastAPI()

#認証
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def auth_request(token: str = Depends(oauth2_scheme)):
    return simple_authentication(token)

#test
@app.get("/")
def rootTest(authentication: bool = Depends(auth_request)):
    if authentication != True:
        return authentication
    return {"test":"OK!"}
    

#　table1リスト取得
# @app.get("/table1")
# def getListTable1(authentication: bool = Depends(auth_request)):
#     if authentication != True:
#         return authentication
#     return session.query(Table1Table).all()

#　table2リスト取得
@app.get("/table2")
def getListTable2(authentication: bool = Depends(auth_request)):
    if authentication == False:
        return HTTPException(status_code=401, detail="authentication_error")
    #TODO 一旦リミットは１００固定
    return session.query(Table2Table).filter(Table2Table.authentication_id == authentication).limit(100).all()

#　table2登録
@app.post("/table2/i")
def post_table2(val:Table2,authentication: bool = Depends(auth_request)):
    if authentication == False:
        return HTTPException(status_code=401, detail="authentication_error")
    insert = Table2Table(authentication_id=authentication,col1=val.col1,col2=val.col2,col3=val.col3)
    result = session.add(insert)
    session.commit()
    return "OK"
