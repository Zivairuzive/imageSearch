import os
import httpx
from .base import ImageProvider
from utils.load_keys import get_value

UNPLASH_ACCESS_KEY = get_value(os.environ.get("UNSPLASH_ACCESS_KEY", ""))
UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"
DEFAULT_EMPTY = []

class UnsplashProvider(ImageProvider):
    
    def __init__(self):
        result = None
        
    async def image_search(self, query:str, per_page:int = 10):
        headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
        params = {"query":query, "per_page":per_page}
        
        with httpx.AsyncClient as client:
            response = await client.get(UNSPLASH_API_URL, headers=headers, params=params)
            response.wait_for_status()
            
        response_data = response.json()
        
        self.results = [
            {
                "id": image['id'],
                "title": query,
                "description": image.get('alt_description', ''),
                "tags":[query],
                "url": image['urls']['full']
                } for image in response_data.get("results", DEFAULT_EMPTY)
        ]
        return self.results

