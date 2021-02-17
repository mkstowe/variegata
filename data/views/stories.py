"""
Variegata Data stories view.
URLs include:
/
"""
import flask
import data
import os


@data.app.route('/', methods=['POST', 'GET'])
def stories():
    """Display / route."""
    files = os.listdir(data.app.config['STORIES_DIR'])

    story_ids = []
    for f in files:
        story_ids.append(f.split('.')[0])

    context = {'stories': story_ids}
    return flask.render_template('stories.html', **context)
