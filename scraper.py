import json
import os
import time
import networkx as nx
import matplotlib.pyplot as plt
import data

from selenium import webdriver
from selenium.webdriver import FirefoxOptions


def click_action(links, action_num):
    links[action_num + 4].click()
    time.sleep(0.2)


class Scraper:
    def __init__(self):
        firefox_options = FirefoxOptions()
        firefox_options.headless = True
        self.driver = webdriver.Firefox(options=firefox_options)

        self.max_depth = 10
        self.end_actions = {
            "End Game and Leave Comments",
            "Click here to End the Game and Leave Comments",
            "See How Well You Did (you can still back-page afterwards if you like)",
            "You have died.",
            "You have died",
            "Epilogue",
            "Save Game",
            "Your quest might have been more successful...",
            "5 - not the best, certainly not the worst",
            "The End! (leave comments on game)",
            "6 - it's worth every cent",
            "You do not survive the journey to California",
            "Quit the game.",
            "7 - even better than Reeses' Cups®",
            "8 - it will bring you enlightenment",
            "End of game! Leave a comment!",
            "Better luck next time",
            "click here to continue",
            "Rating And Leaving Comments",
            "You do not survive your journey to California",
            "Your Outlaw Career has come to an end",
            "Thank you for taking the time to read my story",
            "You have no further part in the story, End Game and Leave Comments",
            "",
            "You play no further part in this story. End Game and Leave Comments",
            "drivers",
            "Alas, poor Yorick, they slew you well",
            "My heart bleeds for you",
            "To End the Game and Leave Comments click here",
            "Call it a day",
            "Check the voicemail.",
            "reset",
            "There's nothing you can do anymore...it's over.",
            "To Be Continued...",
            "Thanks again for taking the time to read this",
            "If you just want to escape this endless story you can do that by clicking here",
            "Boo Hoo Hoo",
            "End.",
            "Pick up some money real quick",
            "",
            "Well you did live a decent amount of time in the Army",
            "End Game",
            "You have survived the Donner Party's journey to California!",
        }
        self.texts = set()

        self.events = []
        self.actions = []
        self.curr_story = ''
        self.event_num = 0
        self.action_num = 0

        self.G = nx.DiGraph()

    def go_to_url(self, url):
        self.texts = set()
        self.driver.get(url)
        time.sleep(0.5)

    def get_text(self):
        div_elements = self.driver.find_elements_by_css_selector("div")
        text = div_elements[3].text
        return text

    def get_links(self):
        return self.driver.find_elements_by_css_selector("a")

    def go_back(self):
        self.get_links()[0].click()
        time.sleep(0.2)

    def get_actions(self):
        return [link.text for link in self.get_links()[4:]]

    def num_actions(self):
        return len(self.get_links()) - 4

    def build_story_tree(self, url):
        scraper.go_to_url(url)
        text = scraper.get_text()

        actions = self.get_actions()

        self.events.append(text)
        self.G.add_node(str(story_num) + "_" + str(self.event_num), text=text)

        story_dict = {"tree_id": url.split('=')[-1], "first_story_block": text, "action_results": []}
        for i, action in enumerate(actions):
            if action not in self.end_actions:
                action_result = self.build_tree_helper(text, i, 0, 0, actions)
                if action_result is not None:
                    story_dict["action_results"].append(action_result)

        return story_dict

    def build_tree_helper(self, parent_story, action_num, depth, prev_event, old_actions):
        depth += 1
        action_result = {}

        action = old_actions[action_num]
        action_result["action"] = action

        links = self.get_links()
        if action_num + 4 >= len(links):
            return None

        click_action(links, action_num)
        result = self.get_text()

        if result == parent_story or result in self.texts:
            self.go_back()
            self.event_num = self.events.index(result)
            self.G.add_edge(str(story_num) + "_" + str(prev_event), str(story_num) + "_" + str(self.event_num))
            return None

        self.events.append(result)
        self.event_num = len(self.events) - 1
        self.G.add_node(str(story_num) + "_" + str(self.event_num), text=result)
        self.G.add_edge(str(story_num) + "_" + str(prev_event), str(story_num) + "_" + str(self.event_num))

        self.texts.add(result)

        action_result["result"] = result

        actions = self.get_actions()
        action_result["action_results"] = []

        for i, action in enumerate(actions):
            if actions[i] not in self.end_actions:
                sub_action_result = self.build_tree_helper(result, i, depth, self.event_num, actions)
                if action_result is not None:
                    action_result["action_results"].append(sub_action_result)

        self.go_back()
        return action_result


def save_tree(tree, filename):
    with open(os.path.join(data.app.config["STORIES_DIR"], filename), "w+") as fp:
        json.dump(tree, fp)


scraper = Scraper()

urls = [
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=5587",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=10638",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=11246",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=54639",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=7397",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=8041",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=11545",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=7393",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=13875",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=37696",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=31013",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=45375",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=41698",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=10634",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=42204",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=6823",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=18988",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=10359",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=5466",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=28030",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=56515",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=7480",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=11274",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=53134",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=17306",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=470",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=8041",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=23928",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=10183",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=45866",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=60232",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=6376",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=36791",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=60128",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=52961",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=54011",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=34838",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=13349",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=8038",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=56742",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=48393",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=53356",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=10872",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=7393",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=31013",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=43910",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=53837",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=8098",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=55043",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=28838",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=11906",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=8040",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=2280",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=31014",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=43744",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=44543",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=56753",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=36594",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=15424",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=8035",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=10524",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=14899",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=9361",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=28030",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=49642",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=43573",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=38025",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=7480",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=7567",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=60747",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=10359",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=31353",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=13875",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=56501",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=38542",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=42204",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=43993",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=1153",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=24743",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=57114",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=52887",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=21879",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=16489",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=53186",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=34849",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=26752",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=7094",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=8557",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=45225",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=4720",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=51926",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=45375",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=27234",
    "http://chooseyourstory.com/story/viewer/default.aspx?StoryId=60772",
]

if os.path.exists(data.app.config["EVENTS_LIST"]):
    os.remove(data.app.config["EVENTS_LIST"])
else:
    print("events.csv does not exist")

for u in range(len(urls)):
    scraper = Scraper()
    story_num = urls[u].split('=')[-1]
    print("** Extracting Adventure", story_num, "**")
    curr_tree = scraper.build_story_tree(urls[u])
    save_tree(curr_tree, str(story_num) + ".json")

    nx.write_adjlist(scraper.G, str(data.app.config["GRAPHS_DIR"]) + '/' + str(story_num) + ".gml")

    with open(data.app.config["EVENTS_LIST"], 'a+') as file:
        for idx, event in enumerate(scraper.events):
            file.write(str(story_num) + ',' + str(idx) + ',' + event.replace('\n', ' ') + '\n')

# plt.figure(figsize=(20, 14))
#
# nx.draw(scraper.G, node_size=1200, node_color='lightblue', linewidths=0.4, font_size=15, with_labels=True,
#         font_weight='bold')
# plt.savefig("story_graph.png")

print("Done")
