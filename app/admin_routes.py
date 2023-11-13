# admin_routes.py
from datetime import datetime
from flask import render_template, url_for, flash, redirect
from app import app, db
from app.models import User, MenuItem
from app.forms import AddMenuItemForm  # You need to create this form

# Admin Dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    # Add logic to check if the user is an admin
    # For example: if current_user.is_admin():
    menu_items = MenuItem.query.all()
    return render_template('admin/dashboard.html', menu_items=menu_items)

# Add Menu Item
@app.route('/admin/menu/add', methods=['GET', 'POST'])
def add_menu_item():
    form = AddMenuItemForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        price = form.price.data
        
        # Handle file upload
        image = form.image.data
        image_filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}.png"  # Adjust the filename as needed
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        image.save(image_path)

        menu_item = MenuItem(name=name, description=description, price=price, image=image_filename)
        db.session.add(menu_item)
        db.session.commit()

        return redirect(url_for('admin_dashboard'))

    return render_template('admin/add_menu_item.html', form=form)

