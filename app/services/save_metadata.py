from app.models.image_metadata import ImageMetadata
from app.db import db
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict

async def save_image_metadata(session: AsyncSession, metadata:List[Dict[str,str]]):
    for meta in metadata:
        existing = await session.execute(
            select(ImageMetadata).where(
                ImageMetadata.provider == meta['provider'],
                ImageMetadata.provider_id == meta['provider_id']
            )
            )
        if existing.scalar_one_or_none():
            continue
        
        image = ImageMetadata(**meta)
        session.add(image)
        
    await session.commit()