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


@quiplash.app.route('/api/v1/resetanswer', methods=["GET"])
def reset_answers():
    """Reset answers for all players.
    """

    context = {}

    # url
    context["url"] = flask.request.path

    # Database
    db = quiplash.model.get_db()

    cur = db.execute(('UPDATE players SET ans1 = \'\', ans2 = \'\' '))

    cur = db.execute("SELECT * FROM players",)
    output = cur.fetchall()

    context["players"] = output

    return flask.jsonify(**context)
