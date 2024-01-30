from sqlalchemy import Column, Integer, String

from app.models.base_model import BaseModel


class Customers(BaseModel):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    address = Column(String)
    email = Column(String)
