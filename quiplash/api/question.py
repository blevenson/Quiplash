"""REST API for questions."""
import flask
import quiplash
import random


@quiplash.app.route('/api/v1/questions', methods=["GET"])
def get_questions():
    """Return list of questions
    """

    num_questions = 1

    # return set number of questions
    if flask.request.json and "num" in flask.request.json:
        num_questions = flask.request.json['num']

    context = {
        "url": "/api/v1/question",
        "questions": []
    }

    questions = []
    for i in range(num_questions):
        questions.append(random.choice(quiplash.QUESTIONS))

    context["questions"] = questions

    return flask.jsonify(**context)
