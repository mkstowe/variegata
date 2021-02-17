"""
Variegata Data story view.
URLs include:
/stories/<id>/
"""
import flask
import data
import os
from json2html import *
import pathlib
import json


@data.app.route('/stories/<story_id>/', methods=['POST', 'GET'])
def story(story_id):
    """Display /stories/<story_id>/ route."""
    with open(str(data.app.config['STORIES_DIR']) + '/' + story_id + '.json') as f:
        content = json.load(f)

    context = {'content': flask.Markup(json2html.convert(json=content)), 'story_id': story_id}
    return flask.render_template('story.html', **context)
