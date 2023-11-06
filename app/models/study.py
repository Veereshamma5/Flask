from sqlalchemy import Column, Integer, Float, DateTime, Index

from app.models.base_model import BaseModel, AuditMixin


class Allocation(BaseModel, AuditMixin):
    __tablename__ = "Student_timetable"
    # Table arguments other than the name, metadata, and mapped Column arguments are specified using the
    # __table_args__ class attribute
    __table_args__ = (
        # Specify index fot the columns syntax:: Index('idx_giventablename_columnname, 'columnname')
        Index('idx_Student_tablename_email', 'email'),
        Index('idx_Student_tablename_base_amount', 'base_amount'),
        Index('idx__Student_tablename_distribution_percentage', 'distribution_percentage'),
        {'schema': 'cdp_tables'}
    )
    initial_percentage = Column(Integer, nullable=True)
    final_percentage = Column(Integer, nullable=True)
    email = Column(DateTime, nullable=False)
    created_on = Column(DateTime, nullable=False)
    base_amount = Column(Float, default=0, nullable=False)
    allocation_date = Column(DateTime, nullable=False)
    distribution_percentage = Column(Integer, nullable=False)
    threshold_amount = Column(Float, nullable=True)





