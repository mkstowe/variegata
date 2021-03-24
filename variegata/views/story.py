"""
Variegata story view.
URLs include:
/story/
"""
import flask
import variegata
from variegata.generator import generate_story


@variegata.app.route('/story/', methods=['GET', 'POST'])
def story():
    """Display /story/ route."""
    context = {"events": generate_story.generate_story(20)}
    return flask.render_template("story.html", **context)
