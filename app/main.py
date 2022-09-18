from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer
from lib.authentication import simple_authentication
from db import session
from model.table1 import Table1, Table1Table
import datetime
import pytz


now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))


app = FastAPI()

# 認証
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def auth_request(token: str = Depends(oauth2_scheme)):
    return simple_authentication(token)

# test
@app.get("/")
def rootTest(authentication: bool = Depends(auth_request)):
    # if authentication != True:
    #     return authentication
    return {"test": "OK!"}


#　table1リスト取得
@app.get("/table1/list")
def getListTable1(authentication: bool = Depends(auth_request)):
    if authentication == False:
        return HTTPException(status_code=401, detail="authentication_error")
    # TODO 一旦リミットは１００固定
    return session.query(Table1Table).filter(Table1Table.authentication_id == authentication, Table1Table.delete_date == None).limit(100).all()

#　table1一件数取得
@app.get("/table1/{id}")
def getListTable1(id:int,authentication: bool = Depends(auth_request)):
    if authentication == False:
        return HTTPException(status_code=401, detail="authentication_error")
    target = session.query(Table1Table).\
        filter(Table1Table.id == id, Table1Table.delete_date == None).first()
    if target:
        return target
    else:
        return "NG"

#　table1登録
@app.post("/table1/create")
def post_table1(val: Table1, authentication: bool = Depends(auth_request)):
    if authentication == False:
        return HTTPException(status_code=401, detail="authentication_error")
    insert = Table1Table(authentication_id=authentication, col1=val.col1, col2=val.col2,
                         col3=val.col3, create_date=now)
    result = session.add(insert)
    session.commit()
    return "OK"

#　table1更新
@app.put("/table1/update")
def put_table1(val: Table1, authentication: bool = Depends(auth_request)):
    if authentication == False:
        return HTTPException(status_code=401, detail="authentication_error")
    target = session.query(Table1Table).\
        filter(Table1Table.id == val.id, Table1Table.delete_date == None).first()
    if target:
        target.col1 = val.col1
        target.col2 = val.col2
        target.col3 = val.col3
        target.update_date = now
        session.commit()
        return "OK"
    else:
        return "NG"

#　table1論理削除
@app.delete("/table1/delete")
def delete_table1(val: Table1, authentication: bool = Depends(auth_request)):
    if authentication == False:
        return HTTPException(status_code=401, detail="authentication_error")
    target = session.query(Table1Table).\
        filter(Table1Table.id == val.id, Table1Table.delete_date == None).first()
    if target:
        target.delete_date = now
        session.commit()
        return "OK"
    else:
        return "NG"
