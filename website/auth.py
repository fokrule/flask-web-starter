from flask import Blueprint, render_template, request, flash, redirect, url_for, session

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login.
    On GET, displays the login form. On POST, processes login attempt.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'user' and password == 'password':
            flash('Logged in successfully!', category='success')
            session['logged_in'] = True  # Set the session variable
            return redirect(url_for('views.home'))
        else:
            flash('Login failed. Check your username and password.', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    """
    Handles user logout.
    """
    session.pop('logged_in', None)  # Remove the session variable
    flash('You have been logged out.', category='info')
    return redirect(url_for('auth.login'))