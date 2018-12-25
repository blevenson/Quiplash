"""REST API for services."""
import flask
import quiplash


@quiplash.app.route('/api/v1/', methods=["GET"])
def get_services():
    """Return list of services.

    Example:
    {
        "url": "/api/v1/"
    }
    """

    context = {
        "url": "/api/v1/"
    }

    return flask.jsonify(**context)
