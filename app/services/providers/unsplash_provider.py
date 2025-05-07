import os
import httpx
from .base import ImageProvider
from utils.load_keys import get_value
from datetime import datetime
from typing import Dict, Union

UNSPLASH_ACCESS_KEY = get_value(os.environ.get("UNSPLASH_ACCESS_KEY", ""))
UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"
DEFAULT_EMPTY = []

class UnsplashProvider(ImageProvider):
    name = "unplash"
    
    def __init__(self):
        result = None
        
    async def image_search(self, query:str, per_page:int = 10):
        headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
        params = {"query":query, "per_page":per_page}
        response_data = get_image_metadata(UNSPLASH_API_URL, headers, params)
        self.results = [
            {   "provider":self.name,
                "provider_id":image['id'],
                "url": image['urls']['full'],
                "title": query,
                "thumbnail_url": image['src'].get('medium'),
                "width": image['width'],
                "height":image['height'],
                "description": image.get('alt_description', ''),
                "fetched_at":datetime.timezone.utcnow(),
                } for image in response_data.get("results", DEFAULT_EMPTY)
        ]
        return self.results
KeyValueStringDictionary = Dict[str, str]

async def get_image_metadata(url: str, headers:KeyValueStringDictionary,
                            params:Dict[str, Union[str,int]])->KeyValueStringDictionary:
    # add logging to signal start of operation
    with httpx.AsyncClient as client:
        response = await client.get(url, headers=headers, params=params)
        response.wait_for_status()
    return response.json()
        
    