## main.py - the main file where i define the app and the endpoints
## main.py contains the api routes (the logic is in services.py)
from fastapi import FastAPI, HTTPException, Query
from typing import List
from services import (
    search_books,
    get_book_details,
    get_book_editions,
    get_author_details,
    view_book_cover,
    check_book_availability,
    sort_books
)
from schemas import SearchQueryParams, SearchResponse
from models import Book, Author, BookEdition, BookCover, Availability


app = FastAPI()

## defining the endpoints

## search books
@app.get("/search-books", response_model=SearchResponse)
async def search_books_endpoint(query_params: SearchQueryParams):
    try:
        return search_books(query_params)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching books: {e}")

## retrieve book details
@app.get("/book/{book_key}", response_model=Book)
async def retrieve_book_details(book_key: str):
    try:
        return get_book_details(book_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving book details: {e}")

## get book editions
@app.get("/book/{book_key}/editions", response_model=List[BookEdition])
async def get_book_editions_endpoint(book_key: str):
    try:
        return get_book_editions(book_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving book editions: {e}")

## get author details
@app.get("/author/{author_key}", response_model=Author)
async def get_author_details_endpoint(author_key: str):
    try:
        return get_author_details(author_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving author details: {e}")

## view book cover
@app.get("/book/{book_key}/cover", response_model=BookCover)
async def view_book_cover_endpoint(book_key: str):
    try:
        return view_book_cover(book_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving book cover: {e}")

## check book availability
@app.get("/book/{book_key}/availability", response_model=Availability)
async def check_book_availability_endpoint(book_key: str):
    try:
        return check_book_availability(book_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error checking book availability: {e}")

## sort books
@app.get("/sort-books", response_model=List[Book])
async def sort_books_endpoint(
    books: List[Book], sort_by: str = Query("title", alias="sort")
):
    try:
        return sort_books(books, sort_by)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sorting books: {e}")
