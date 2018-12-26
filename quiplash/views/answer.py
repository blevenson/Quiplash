"""
Quiplash answer view.

URLs include:
/
"""
import flask
import quiplash


@quiplash.app.route('/answer', methods=['GET', 'POST'])
def show_answer_form():
    """Display /answer route."""
    context = {
    }

    # Check is user not joined game
    if 'username' not in flask.session:
        return flask.redirect('/')

    if flask.request.method == 'POST':
        # Get Username and password
        ans1 = flask.request.form['ans1']
        ans2 = flask.request.form['ans2']

        connection = quiplash.model.get_db()

        # Store question answers
        connection.execute(('UPDATE players SET ans1 = \'%s\', ans2 = \'%s\' WHERE name = \'%s\'')
                           % (ans1, ans2, flask.session['username']))

        return flask.redirect('/play')

    context['q1'] = "Question 1"
    context['q2'] = "Question 2"

    return flask.render_template("answer.html", **context)
