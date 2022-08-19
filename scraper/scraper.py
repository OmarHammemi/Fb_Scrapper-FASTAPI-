from utils import *
from selenium.webdriver.common.by import By


class FacebookScraper:
    """A class used to represent a single page scraper."""

    def __init__(self, page_name: str, timeout: int):

        self.driver = None
        self.page_name = page_name
        self.URL = get_full_path(page_name)
        self.timeout = timeout

    def init_driver(self):
        """ Initialize the driver """
        download_chrome_driver()
        self.driver = initialize_driver()
        self.driver.get(self.URL)
        scroll_down_first(self.driver)
        close_error_popup(self.driver)

    def scrape_data(self):
        data = {}

        all_posts = self.driver.find_elements(By.CSS_SELECTOR, '[aria-posinset]')
        for index, post in enumerate(all_posts):
            id_ = index
            text = get_text(post)
            video = get_link_video(post)
            shares, comments = get_shares_comments(post)
            total_reactions = get_reactions(post)
            posted_time = get_posted_time(post)
            images = get_images(post)

            data[id_] = {
                "page_name": self.page_name,
                "shares": shares,
                "reaction_count": total_reactions,
                "comments": comments,
                "content": text,
                "posted_on": posted_time,
                "video": video,
                "image": images,
            }
        return data
