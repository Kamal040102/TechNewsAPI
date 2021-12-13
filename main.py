from fastapi import FastAPI
from Scraper import Scraper
from fastapi.middleware.cors import CORSMiddleware
from MultipageScraper import MultipageScraper


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

news = Scraper()
multipagenews = MultipageScraper()

@app.get("/")
def printNews():
    return news.getNews()

@app.get("/{page}")
def printNews(page):
    return news.getNews() if page == '1' else multipagenews.getNews(page)