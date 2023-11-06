from datetime import datetime
from uuid import uuid4

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

DB = SQLAlchemy()
MIGRATE = Migrate()


class BaseModel(DB.Model):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class AuditMixin(DB.Model):
    __abstract__ = True

    created_on = Column(DateTime, default=datetime.now)
    modified_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.now)
