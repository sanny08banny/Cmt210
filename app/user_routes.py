# user_routes.py
from flask import render_template, url_for
from app import app
from app.models import MenuItem

# User Dashboard
@app.route('/user/dashboard')
def user_dashboard():
    # Add logic to check if the user is logged in
    # For example: if current_user.is_authenticated:
    menu_items = MenuItem.query.all()
    return render_template('user/dashboard.html', menu_items=menu_items)

