import uuid
from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ImageMetadata(Base):
    __table_name__ = "image_metadata"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(String, nullable=True)
    provider_id = Column(String, nullable=True)
    url = Column(String, nullable=False)
    thumbnail = Column(String, nullable=True)
    width = Column(Integer)
    height = Column(Integer)
    description = Column(Text)
    fetched_at = Column(DateTime, default = datetime.timezone.utc())
    
    