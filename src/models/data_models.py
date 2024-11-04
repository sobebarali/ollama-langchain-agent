from pydantic import BaseModel, Field
from typing import List, Optional

class Restaurant(BaseModel):
    name: str
    description: Optional[str] = None
    cuisine: Optional[str] = None
    price_range: Optional[str] = None
    location: Optional[str] = None
    rating: Optional[float] = None

class SearchQuery(BaseModel):
    query: str
    location: Optional[str] = None
    cuisine: Optional[str] = None
    price_range: Optional[str] = None

class SearchResult(BaseModel):
    query: SearchQuery
    restaurants: List[Restaurant] = Field(default_factory=list)
