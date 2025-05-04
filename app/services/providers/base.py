# base implementation for the image providers 
from abc import ABC, abstractmethod
from typing import List, Dict


class ImageProvider(ABC):
    
    @abstractmethod
    async def image_search(self, query:str, per_page:int = 10 ): List[Dict[str:str|[str]]]
    '''
    Perform a search and return list of image metadata
    [
        {
            'id':'123',
            'title':'africa',
            'description':'Beautiful Africa',
            'tags':['sunset','nature']
        },
        ...
    ]
    '''
    pass
    