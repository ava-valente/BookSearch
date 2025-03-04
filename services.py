## services.py - where i structure the actual communication with the api
## services.py contains the logic (the api routes are in main.py)
import requests
from typing import List
from models import Book, Author, BookEdition, BookCover, Availability, SearchResponse
from schemas import SearchQueryParams

OPEN_LIBRARY_URL = "https://openlibrary.org"

## search books
def search_books(query_params: SearchQueryParams) -> SearchResponse:
    params = query_params.dict()
    response = requests.get(f"{OPEN_LIBRARY_URL}/search.json", params=params)
    data = response.json()
    books = [Book(**book) for book in data['docs']]
    return SearchResponse(num_found=data['numFound'], docs=books)

## get book details
def get_book_details(book_key: str) -> Book:
    response = requests.get(f"{OPEN_LIBRARY_URL}/works/{book_key}.json")
    data = response.json()
    return Book(**data)

## get book editions
def get_book_editions(book_key: str) -> List[BookEdition]:
    response = requests.get(f"{OPEN_LIBRARY_URL}/works/{book_key}/editions.json")
    data = response.json()
    editions = [BookEdition(**edition) for edition in data['entries']]
    return editions

## get author details
def get_author_details(author_key: str) -> Author:
    response = requests.get(f"{OPEN_LIBRARY_URL}/authors/{author_key}.json")
    data = response.json()
    return Author(**data)

## view book cover
def view_book_cover(book_key: str) -> BookCover:
    response = requests.get(f"{OPEN_LIBRARY_URL}/works/{book_key}.json")
    data = response.json()
    cover_id = data.get('cover_id')
    if cover_id:
        cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
        return BookCover(cover_url=cover_url)
    return BookCover(cover_url="")

## check book availability
def check_book_availability(book_key: str) -> Availability:
    response = requests.get(f"{OPEN_LIBRARY_URL}/works/{book_key}/available.json")
    data = response.json()
    return Availability(is_available=data['available'])

## sort books
def sort_books(books: List[Book], sort_by: str) -> List[Book]:
    if sort_by == "title":
        return sorted(books, key=lambda book: book.title)
    return books
