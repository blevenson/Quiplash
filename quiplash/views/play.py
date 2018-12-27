"""
Quiplash play view.

URLs include:
/
"""
import flask
import quiplash


@quiplash.app.route('/play', methods=['GET'])
def show_play():
    """Display /play route."""
    context = {
    }

    # Check is user joined game
    if 'username' not in flask.session:
        return flask.redirect('/join')

    return flask.render_template("play.html", **context)


@quiplash.app.route('/join', methods=['GET', 'POST'])
def show_join():
    """Display /join route."""
    context = {
    }

    connection = quiplash.model.get_db()

    # Check is user already joined game
    if 'username' in flask.session and quiplash.model.check_exists(connection, flask.session['username']):
        return flask.redirect('/play')

    if flask.request.method == 'POST':
        # Get Username
        username_input = flask.request.form['username']

        cursor = connection.cursor()

        cursor.execute('INSERT INTO players(name, points, ans1, ans2) VALUES(\'' +
                       username_input + '\', 0, \'\',\'\')',)

        flask.session['username'] = username_input

        return flask.redirect('/play')

    return flask.render_template("join.html", **context)


@quiplash.app.route('/vote', methods=['GET', 'POST'])
def show_vote():
    """Display /vote route."""
    context = {}

    connection = quiplash.model.get_db()

    # Check is user already joined game
    if 'username' not in flask.session:
        return flask.redirect('/')

    if flask.request.method == 'POST':
        # Get vote, 1 or 2
        username_input = flask.request.form['username']

        cursor = connection.cursor()

        cursor.execute('INSERT INTO players(name, points, ans1, ans2) VALUES(\'' +
                       username_input + '\', 0, \'\',\'\')',)

        flask.session['username'] = username_input

        return flask.redirect('/play')

    context['id1'] = "player1id"
    context['id2'] = "player2id"

    context['ans1'] = "player1ans"
    context['ans2'] = "player2ans"

    return flask.render_template("vote.html", **context)
