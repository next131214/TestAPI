from datetime import date, datetime
from unicodedata import decimal
from sqlalchemy import Column, Integer, String, DATE, DATETIME ,FLOAT,TEXT,DECIMAL
from pydantic import BaseModel
from db import Base
from db import ENGINE

# テーブル定義
class Table1Table(Base):
    __tablename__ = 'table1'
    id = Column(Integer, primary_key=True, autoincrement=True)
    col_unique = Column(String(255))
    col1 = Column(String(255))
    col2 = Column(String(255))
    col3 = Column(String(255))
    col4 = Column(String(255))
    col5 = Column(String(255))
    col6 = Column(String(255))
    col7 = Column(String(255))
    col8 = Column(String(255))
    col9 = Column(String(255))
    col10 = Column(String(255))
    col_flag1 = Column(Integer)
    col_flag2 = Column(Integer)
    col_flag2 = Column(Integer)
    col_date1 = Column(DATE)
    col_date2 = Column(DATE)
    col_date3 = Column(DATE)
    col_datetime1 = Column(DATETIME)
    col_datetime2 = Column(DATETIME)
    col_datetime3 = Column(DATETIME)
    col_int1 = Column(Integer)
    col_int2 = Column(Integer)
    col_int3 = Column(Integer)
    col_decimal = Column(DECIMAL)
    col_double = Column(FLOAT)
    col_float = Column(FLOAT)
    col_text1 = Column(TEXT)
    col_text2 = Column(TEXT)
    col_text3 = Column(TEXT)

# モデル定義 
class Table1(BaseModel):
    id: int
    col_unique:str
    col1:str
    col2:str
    col3:str
    col4:str
    col5:str
    col6:str
    col7:str
    col8:str
    col9:str
    col10:str
    col_flag1:bool
    col_flag2:bool
    col_flag2:bool
    col_date1:date
    col_date2:date
    col_date3:date
    col_datetime1:datetime
    col_datetime2:datetime
    col_datetime3:datetime
    col_int1:int
    col_int2:int
    col_int3:int
    col_decimal:float
    col_double:float
    col_float:float
    col_text1:str
    col_text2:str
    col_text3:str

def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()