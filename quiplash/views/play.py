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
        # Get Username and password
        username_input = flask.request.form['username']

        cursor = connection.cursor()

        cursor.execute('INSERT INTO players(name, points, ans1, ans2) VALUES(\'' +
                       username_input + '\', 0, \'\',\'\')',)

        flask.session['username'] = username_input

        return flask.redirect('/play')

    return flask.render_template("join.html", **context)
