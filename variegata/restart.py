from scraper import scrape_stories
from merge_graphs import merge_graphs
from model.create_model import create_model

print("SCRAPING STORIES")
scrape_stories()
print("MERGING STORIES")
merge_graphs()
print("CREATING MODEL")
create_model()
