import os

from create_graphs import construct_graph
# from database import get_db
from model.create_model import create_model
from scraper import scrape_stories


def restart():
    # clear_db()
    clear_dirs()

    print("SCRAPING STORIES")
    scrape_stories()
    print("CONSTRUCTING KEYWORD GRAPH")
    construct_graph()
    print("CREATING MODEL")
    create_model()


# def clear_db():
#     print("RESETTING DATABASE")
#     conn = get_db()
#
#     cursor = conn.cursor()
#     cursor.execute("DROP TABLE IF EXISTS events;")
#     cursor.execute("""
#             CREATE TABLE events(
#                 id INTEGER AUTO_INCREMENT PRIMARY KEY,
#                 event_idx INTEGER,
#                 story_num VARCHAR(16) NOT NULL,
#                 text TEXT
#             );
#         """)
#     conn.commit()
#     conn.close()


def clear_dirs():
    print("CLEARING STORY DIRECTORY")
    for f in os.listdir("static/stories"):
        os.remove(os.path.join("static/stories", f))

    print("CLEARING GRAPH DIRECTORY")
    for f in os.listdir("static/graphs"):
        os.remove(os.path.join("static/graphs", f))


restart()
