## schemas.py -  adding this for the sorting and other results that require it
from pydantic import BaseModel
from typing import Optional

## needed this, according to the api's documentation
class SearchQueryParams(BaseModel):
    q: str
    start: Optional[int] = 0
    rows: Optional[int] = 10
    sort: Optional[str] = "title"
