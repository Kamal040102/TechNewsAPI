from bs4 import BeautifulSoup
import requests

class MultipageScraper():
    def getNews(self, page):
        url = requests.get(f"https://www.gadgetsnow.com/tech-news/{page}").text

        newsListMain = []

        soup = BeautifulSoup(url, "lxml")
        newsListDiv = soup.find('div', class_="tech_list ctn_stories")
        newsList = newsListDiv.find("ul", class_="cvs_wdt")
        newsComponent = newsList.find_all('li')
        for newsItem in newsComponent:
            newsTitle = newsItem.find('span', class_="w_tle").text
            newsDesc = newsItem.find('span', class_="w_desc").text
            newsImgTag = newsItem.find('a', class_="w_img")
            newsURLtoIMG = newsImgTag.find('img')['src']
            newsURL = newsImgTag['href']

            item = {
                "newsTitle": newsTitle,
                "newsDesc":newsDesc,
                "newsURLtoIMG": newsURLtoIMG,
                "newsURL": f"https://www.gadgetsnow.com{newsURL}"
            }

            newsListMain.append(item)

        JSONresult = {
                "source":"https://www.gadgetsnow.com",
                "articles":newsListMain
            }
        return JSONresult

# newsScraper = Scraper()
# newsScraper.getNews(page)