"""REST API for players."""
import flask
import quiplash


@quiplash.app.route('/api/v1/players', methods=["GET"])
def get_players():
    """Return list of players.

    Example:
    {
        "url": "/api/v1/"
    }
    """

    context = {}

    # url
    context["url"] = flask.request.path

    # Database
    db = quiplash.model.get_db()

    cur = db.execute("SELECT * FROM players",)
    output = cur.fetchall()

    context["players"] = output

    return flask.jsonify(**context)
