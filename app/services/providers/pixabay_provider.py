import os
import httpx
from .base import ImageProvider
from typing import List, Dict
from datetime import datetime

DEFAULT_EMPTY = []
PIXABAY_API_KEY = os.environ.get("PIXABEY_API_KEY", "")
PIXABAY_API_URL = "https://pixabay.com/api"

if PIXABAY_API_KEY == "":
    raise ValueError(f"expected an API KEY but got an empty value")


class PixabayProvider(ImageProvider):
    name = "pixabay"
    
    def __init__(self):
        results = None
        
    async def image_search(self, query:str, per_page:int=10):
        params ={
            "key":PIXABAY_API_KEY,
            "q": query,
            "per_page": per_page,
            "imagetype":"photo",
        }
        
        with httpx.AsyncClient as client:
            response = await client.get(PIXABAY_API_URL, params=params)
            response.raise_for_status()
            
        response_data = response.json()
        self.results = [
            {   
                "provider": self.name,
                "provider_id": str(image['id']),
                "url":image.get("largeImageURL"),
                "title":query,
                "thumbnail_url": image["previewURL"],
                "width":image.get("imageWidth"),
                "height": image.get("imageHeight"),
                "description":image.get('tags', ''),
                "fetched_at": datetime.timezone.utcnow(),
            }
            for image in response_data.get('hits', DEFAULT_EMPTY)
        ]
        return self.results