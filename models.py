# This file defines the database structure for assignment entity using SQLite
# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Assignment(db.Model):
    _tablename_ = 'assignments'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Required Fields
    title = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    
    # Optional Fields
    description = db.Column(db.Text, nullable=True)
    priority = db.Column(db.String(10), default='Medium') # e.g., 'High', 'Medium', 'Low'
    
    # Status/Tracking Fields
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def _repr_(self):
        return f"<Assignment {self.title} - Due: {self.due_date.strftime('%Y-%m-%d')}>"
