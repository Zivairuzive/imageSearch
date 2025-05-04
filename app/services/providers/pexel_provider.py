import os
import requests, httpx
from typing import List, Dict
from .base import ImageProvider

PEXEL_API_KEY = os.environ.get('PEXEL_API_KEY', "")
EMPTY = []

if PEXEL_API_KEY == "":
    raise ValueError(f"expected an value not ${PEXEL_API_KEY}")

PEXEL_BASE_API_URL = "https://api.pexels/api/v1"

class PexelProvider(ImageProvider):
    
    def __init__(self):
        results = []
    
    async def search_image(self, query, per_page):
        headers = {'Authorization': PEXEL_API_KEY}
        params = {"query":query, "per_page": per_page}
        
        with httpx.AsyncClient as client:
            response = await client.get(PEXEL_BASE_API_URL,params=params,headers=headers) 
            response.raise_for_status()
        
        for photo in response.json().get('photos', EMPTY):
            self.results.append(
                {
                    "id":photo.id,
                    "title":query,
                    "description":photo.get("alt", EMPTY),
                    "tags": [query],
                    "url":photo["src"]["original"]
                }
            )
        return self.results
            
            
        
        

