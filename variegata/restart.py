from scraper import scrape_stories
from merge_graphs import merge_graphs
from model.create_model import create_model
from database import get_db
import mariadb
import os


def restart():
    print("RESETTING DATABASE")
    conn = get_db()

    # Get Cursor
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS events;")
    cursor.execute("""
        CREATE TABLE events(
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            story_num VARCHAR(16) NOT NULL,
            event_idx INTEGER,
            text TEXT
        );
    """)
    conn.commit()
    conn.close()

    print("CLEARING STORY DIRECTORY")
    for f in os.listdir("static/stories"):
        os.remove(os.path.join("static/stories", f))

    print("CLEARING GRAPH DIRECTORY")
    for f in os.listdir("static/graphs"):
        os.remove(os.path.join("static/graphs", f))

    print("SCRAPING STORIES")
    scrape_stories()
    print("MERGING STORIES")
    merge_graphs()
    print("CREATING MODEL")
    create_model()


restart()
