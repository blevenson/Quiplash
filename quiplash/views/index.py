"""
Quiplash server index (main) view.

URLs include:
/
"""
import flask
import quiplash
import flask


@quiplash.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Display / route."""
    context = {
    }

    return flask.render_template("index.html", **context)
