from flask import Blueprint, render_template
import random # Import random to pick a random quote

views = Blueprint('views', __name__)

@views.route('/')
def home():
    """
    Renders the homepage of the application.
    """
    return render_template("home.html")

@views.route('/about')
def about():
    """
    Renders the about page.
    """
    return render_template("about.html")

@views.route('/quote')
def quote():
    """
    Generates and renders a random inspirational quote.
    """
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Strive not to be a success, but rather to be of value. - Albert Einstein",
        "The best way to predict the future is to create it. - Peter Drucker"
    ]
    random_quote = random.choice(quotes)
    return render_template("quote.html", quote=random_quote)