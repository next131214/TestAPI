from datetime import date, datetime
from typing import Union
from unicodedata import decimal
from sqlalchemy import Column, Integer, String, DATE, DATETIME ,FLOAT,TEXT,DECIMAL
from pydantic import BaseModel
from db import Base
from db import ENGINE

# テーブル定義
class Table2Table(Base):
    __tablename__ = 'table2'
    id = Column(Integer, primary_key=True, autoincrement=True)
    authentication_id = Column(Integer)
    col1 = Column(String(255))
    col2 = Column(String(255))
    col3 = Column(String(255))


class Table2(BaseModel):
    # id:Union[int, None] = None   
    authentication_id:Union[int, None] = None    
    col1:Union[str, None] = None
    col2:Union[str, None] = None
    col3:Union[str, None] = None
    class Config:
        orm_mode = True

def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()