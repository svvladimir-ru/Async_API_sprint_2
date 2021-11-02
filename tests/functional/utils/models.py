from typing import Optional
from datetime import date

from dataclasses import dataclass
from pydantic import BaseModel
from multidict import CIMultiDictProxy


@dataclass
class HTTPResponse:
    body: dict
    headers: CIMultiDictProxy[str]
    status: int


class Film(BaseModel):
    id: str
    imdb_rating: float
    genre: Optional[list[dict[str, str]]] = None
    title: str
    description: Optional[str] = None
    director: Optional[list[dict[str, str]]] = None
    actors_names: Optional[list[str]] = None
    writers_names: Optional[list[str]] = None
    actors: Optional[list[dict[str, str]]] = None
    writers: Optional[list[dict[str, str]]] = None


class FilmShort(BaseModel):
    id: str
    title: str
    imdb_rating: Optional[float] = None


class Person(BaseModel):
    id: str
    full_name: str
    birth_date: Optional[date] = None
    role: Optional[str] = None
    film_ids: list[str]


class Genre(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
