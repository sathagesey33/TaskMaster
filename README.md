# TaskMaster - Task Management System

**TaskMaster** is an intuitive and powerful task management system built to help teams and individuals efficiently organize, track, and manage tasks and projects. With features like Google OAuth authentication, task creation, progress tracking, tagging, and deadline reminders, TaskMaster is the ideal productivity tool to keep you on top of your work.

---

## 🚀 Features

- **User Authentication**: Secure login via Google OAuth 2.0.
- **Task Creation**: Easily create tasks and assign them to team members.
- **Task Tracking**: Track progress and deadlines, ensuring you never miss a due date.
- **Tags & Categorization**: Organize tasks with custom tags and categories.
- **Progress Updates**: Mark tasks as in progress, completed, or pending.
- **Deadline Reminders**: Get notified about upcoming deadlines and overdue tasks.
- **Admin Interface**: Manage users, tasks, and monitor overall progress via the Django admin panel.

---

## 🔧 Tech Stack

- **Backend**: Django 5.1.2 + Django REST Framework
- **Authentication**: Google OAuth 2.0, JWT Authentication
- **Database**: PostgreSQL
- **Deployment**: Docker & Docker Compose
- **CI/CD**: GitHub Actions

---

## 🧑‍💻 Installation

### ✅ Prerequisites

- Python 3.11+
- Docker & Docker Compose
- PostgreSQL

---

### 📦 Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/sathagesey33/TaskMaster.git
cd TaskMaster
```

#### 2. Create a `.env` File

Create a `.env` file in the project root with the following:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_NAME=taskmaster_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=db
DATABASE_PORT=5432

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback/
```

#### 3. Build and Run with Docker

```bash
docker-compose up --build
```

This sets up Django, PostgreSQL, and installs all dependencies.

#### 4. Apply Migrations

```bash
docker-compose exec web python manage.py migrate
```

#### 5. Create a Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

---

### 🌐 Access the App

- Main App: [http://localhost:8000](http://localhost:8000)
- Admin Panel: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🔐 Google OAuth Authentication

### Step 1: Obtain Google Client ID and Secret

To use Google OAuth, you need to create credentials in the Google Cloud Console:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services > Credentials**.
4. Click **Create Credentials** and select **OAuth 2.0 Client IDs**.
5. Configure the consent screen and set the redirect URI to `http://localhost:8000/auth/callback/`.
6. Once created, you'll get a **Client ID** and **Client Secret**.

For a detailed step-by-step guide, refer to [Google's official documentation](https://developers.google.com/identity/protocols/oauth2).

### Step 2: Get Authorization Code

Open this in your browser (replace with your Client ID):

```
https://accounts.google.com/o/oauth2/v2/auth?client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:8000/auth/callback/&response_type=code&scope=openid%20email%20profile&access_type=offline&prompt=consent
```

Log in and authorize. You'll be redirected to:

```
http://localhost:8000/auth/callback/?code=AUTH_CODE
```

### Step 3: Exchange Code for Token

Make a POST request to exchange the code for a JWT:

```bash
curl -X POST http://localhost:8000/api/auth/google/login/ \
  -H "Content-Type: application/json" \
  -d '{"code": "YOUR_AUTH_CODE"}'
```

Response:

```json
{
  "token": "your-jwt-token",
  "user": {
    "id": 1,
    "email": "your_email@gmail.com"
  }
}
```

### Step 4: Access Protected Routes

```bash
curl http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer your-jwt-token"
```

---

## 🐳 Useful Docker Commands

- Start containers: `docker-compose up`
- Stop containers: `docker-compose down`
- View logs: `docker-compose logs -f`
- Run management command: `docker-compose exec web python manage.py <command>`

---

## 🤖 CI/CD Pipeline

This project includes a GitHub Actions workflow for:

- Linting and running tests on each push
- Automated build process
- Future deployment pipeline (extendable)

---

