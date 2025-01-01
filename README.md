TaskMaster - Task Management System

TaskMaster is an intuitive and powerful task management system built to help teams and individuals efficiently organize, track, and manage tasks and projects. With features like user authentication, task creation, progress tracking, tagging, and deadline reminders, TaskMaster is the ideal productivity tool to keep you on top of your work.
🚀 Features

    User Authentication: Secure sign-up, login, and authentication system.
    Task Creation: Easily create tasks and assign them to team members.
    Task Tracking: Track progress and deadlines, ensuring you never miss a due date.
    Tags & Categorization: Organize tasks with custom tags and categories.
    Progress Updates: Mark tasks as in progress, completed, or pending.
    Deadline Reminders: Get notified about upcoming deadlines and overdue tasks.
    Admin Interface: Manage users, tasks, and monitor overall project progress through an easy-to-use Django admin panel.

🔧 Tech Stack

    Backend: Django 5.1.2
    Database: PostgreSQL
    Deployment: Docker, Docker Compose
    API Security: JWT Authentication
    CI/CD: GitHub Actions

🧑‍💻 Installation

Follow the steps below to get the application up and running on your local machine.
Prerequisites

    Docker and Docker Compose
    Python 3.11+
    PostgreSQL

Step-by-Step Setup

    Clone the Repository

git clone https://github.com/yourusername/taskmaster.git
cd taskmaster

Build and Run Docker Containers

Run the following command to build and start the Docker containers for both the application and the database:

docker-compose up --build

This will set up the environment with PostgreSQL and Django, including all the necessary dependencies.

Apply Migrations

After the containers are running, apply the migrations to set up the database:

docker-compose exec web python manage.py migrate

Create a Superuser

Create an admin user to access the Django admin interface:

    docker-compose exec web python manage.py createsuperuser

    Follow the prompts to create the superuser with a username, email, and password.

    Access the Application

    Open your browser and go to http://localhost:8000 to view the app. You can log in to the Django admin panel at http://localhost:8000/admin/ using the superuser credentials you created.

📦 Docker Commands

    Start containers: docker-compose up
    Stop containers: docker-compose down
    View logs: docker-compose logs -f
    Execute a command in the container: docker-compose exec web <command>

🤖 CI/CD

This project integrates CI/CD pipelines with GitHub Actions to automate testing, building, and deployment processes.