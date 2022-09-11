
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE

# テーブル定義
class AuthenticationTable(Base):
    __tablename__ = 'authentication'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key_id = Column(String(255), nullable=False)
    key_code = Column(String(255), nullable=False)
    key_pass = Column(String(255), nullable=False)

# モデル定義 
class Authentication(BaseModel):
    id: int
    key_id: str
    key_code: str
    key_pass: str


def main():
    # テーブル構築
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()