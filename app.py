#This file sets up the Flask application, configures the database, and defines the routes for CRUD (Create, Read, Update, Delete).
# app.py

from flask import Flask, render_template, request, redirect, url_for
from models import db, Assignment
from datetime import datetime

# --- Configuration ---
app = Flask(_name_)
# Using SQLite for a simple example. Replace with PostgreSQL/MySQL for production.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Helper function to convert form date/time strings to a datetime object
def parse_due_date(date_str, time_str):
    combined_str = f"{date_str} {time_str}"
    # Handles form input formats like '2025-12-31 23:59'
    return datetime.strptime(combined_str, '%Y-%m-%d %H:%M')


# --- Routes (Endpoints) ---

@app.before_first_request
def create_tables():
    """Ensure the database tables are created before the first request."""
    db.create_all()

# 1. READ (Assignment List/Dashboard)
@app.route('/')
def assignment_list():
    """Display all pending assignments, sorted by due date."""
    assignments = Assignment.query.filter_by(is_completed=False).order_by(Assignment.due_date).all()
    completed = Assignment.query.filter_by(is_completed=True).count()
    return render_template('dashboard.html', assignments=assignments, completed_count=completed)

# 2. CREATE (Add New Assignment)
@app.route('/add', methods=['GET', 'POST'])
def add_assignment():
    if request.method == 'POST':
        try:
            # Simple form validation (Essential part of Technical Expectations)
            if not request.form['title'] or not request.form['due_date'] or not request.form['due_time']:
                # Handle error: Missing required field
                return "Missing required fields (Title, Due Date, Time)", 400

            due_datetime = parse_due_date(request.form['due_date'], request.form['due_time'])

            new_assignment = Assignment(
                title=request.form['title'],
                course=request.form['course'],
                due_date=due_datetime,
                description=request.form['description'],
                priority=request.form.get('priority', 'Medium')
            )
            db.session.add(new_assignment)
            db.session.commit()
            return redirect(url_for('assignment_list'))
            
        except ValueError:
            return "Invalid Date/Time Format", 400

    return render_template('add_assignment.html')

# 3. UPDATE (Toggle Completion Status)
@app.route('/complete/<int:assignment_id>')
def complete_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    assignment.is_completed = True
    db.session.commit()
    return redirect(url_for('assignment_list'))

# 4. DELETE (Remove Assignment)
@app.route('/delete/<int:assignment_id>')
def delete_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    db.session.delete(assignment)
    db.session.commit()
    return redirect(url_for('assignment_list'))

if _name_ == '_main_':
    # When running the application for the first time, uncomment the lines below
    # to create the database file and table.
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
