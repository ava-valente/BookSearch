## models.py - defining the models for the endpoints (the inputs/outputs)
from pydantic import BaseModel
from typing import List, Optional

## went through the api documentation and made classes based off the required data
class Book(BaseModel):
    title: str
    author_name: Optional[str] = None
    publish_date: Optional[str] = None
    key: str


class Author(BaseModel):
    name: str
    birth_date: Optional[str] = None
    death_date: Optional[str] = None
    key: str


class BookEdition(BaseModel):
    title: str
    language: Optional[str] = None
    publisher: Optional[str] = None
    key: str


class BookCover(BaseModel):
    cover_url: str


class Availability(BaseModel):
    is_available: bool
    library_url: Optional[str] = None


class SearchResponse(BaseModel):
    num_found: int
    docs: List[Book]
