# 🔔 Academic Assignment Reminder System

## Project Overview
The Academic Assignment Reminder System is a web-based application designed to help students efficiently manage their academic workload. It addresses the common challenge of tracking deadlines scattered across various sources by providing a centralized platform for scheduling, visualizing, and receiving timely notifications for all assignments.

## ✨ Features

* *Assignment CRUD:* Full *Create, **Read, **Update, and **D*elete functionality for tracking assignments.
* *Deadline Visualization:* Calendar and list views to clearly see upcoming and overdue assignments.
* *Custom Notification Preferences:* Users can set multiple, configurable reminders (e.g., 48 hours and 1 hour before) via email or in-app alerts.
* *Dashboard Analytics:* Quick overview of completion rates and pending assignments.

## 🛠 Technologies & Tools Used

* *Backend:* Python, Flask (or Django)
* *Database:* PostgreSQL (for data reliability and structure)
* *Asynchronous Tasks:* Redis/Celery (for reliable, scheduled notification processing)
* *Frontend:* HTML, CSS, JavaScript, Jinja2 templating
* *Version Control:* Git

## ⚙ Steps to Install & Run the Project

Follow these steps to set up and run the application locally:

1.  *Clone the Repository:*
    bash
    git clone [your-repo-link]
    cd academic-reminder-system
    

2.  *Setup Environment & Dependencies:*
    bash
    # Create and activate a virtual environment
    python3 -m venv venv
    source venv/bin/activate 

    # Install required packages
    pip install -r requirements.txt
    

3.  *Database Configuration:*
    * Ensure PostgreSQL is running.
    * Create a database named assignment_db.
    * Set the database connection string in a file named .env (refer to settings_template.env).

    bash
    # Run migrations to set up tables
    python manage.py migrate
    

4.  *Run the Application:*
    * Start the main application server:
        bash
        python manage.py runserver
        
    * Start the notification worker (in a separate terminal):
        bash
        celery -A your_app_name worker -l info
        
    * Access the application at http://127.0.0.1:5000 (or the default Flask/Django port).

## 🧪 Instructions for Testing

To ensure the core functionality is working correctly, run the provided unit tests:

```bash
# Ensure dependencies are installed and the virtual environment is active
pytest
