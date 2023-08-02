from bs4 import BeautifulSoup
import lxml
import requests
import json
import psycopg2
from config import host, user, password, db_name

class animegoParse():
    headers__ = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    season = "" # winter // spring // summer // fall
    year = "" # год
    anime_name = ""
    anime_href = ""
    anime_img_href = ""
    anime_genre = ""

    def __init__(self, season, year):
        self.season = season
        self.year = year

    def ged_data(self):
        for page in range(4):
            if page == 0:
                continue
            url = f"https://animego.org/anime/season/{self.year}/{self.season}?sort=a.createdAt&direction=desc&type=animes&page={page}"
            req = requests.get(url, headers = self.headers__)
            req.encoding = "utf8"
            src = req.text

            soup = BeautifulSoup(src, "lxml")
            all_anime_hrefs = soup.findAll(class_ = "h5 font-weight-normal mb-1")
            all_anime_images = soup.findAll(class_ = "anime-list-lazy lazy")
            all_anime_genres_info = soup.findAll(class_ = "anime-genre d-none d-sm-inline")

            all_anime_data_list = []
            for item, image, genre in zip(all_anime_hrefs, all_anime_images, all_anime_genres_info):
                item_text = item.text
                item_href = item.next_element.get("href")
                item_image = image['data-original']
                item_genre = genre.text.replace(' ', '').replace(',', ' , ')
                self.anime_name = item_text
                self.anime_href = item_href
                self.anime_img_href = item_image
                self.anime_genre = item_genre
                self.connect_to_db()

                all_anime_data_list.append((item_text, item_href, item_image, item_genre))
            print(all_anime_data_list)

            with open(f"all_anime_list_{self.year}_{self.season}_{page}.json", "w", encoding="utf8") as file:
                json.dump(all_anime_data_list, file, indent=4, ensure_ascii=False)
    def connect_to_db(self):
        insert_query = """
            INSERT INTO main_anime_list (name, anime_href, img_href, season, year, genre)
            VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (name) DO NOTHING;
        """
        try:
            connection = psycopg2.connect(
                host = host,
                user = user,
                password = password,
                database = db_name
            )
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute(insert_query,
                               (self.anime_name,
                                self.anime_href,
                                self.anime_img_href,
                                self.season,
                                self.year,
                                self.anime_genre))
                print(f"[INFO] Anime {self.anime_name} is add")
        except Exception as _ex:
            print("[INFO] error while working with PGSQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] PGSQL connection closed")

def main():
    testClass = animegoParse(season= "fall", year="2023")
    testClass.ged_data()

if __name__ == "__main__":
    main()
