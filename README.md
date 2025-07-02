# NoteSwap

"NoteSwap" – Peer-to-Peer Lecture Notes Exchange
🎯 Problem:
Students miss lectures or want different perspectives, but there’s no easy way to share or find quality notes.

✅ Solution:
A web app where students can:

Upload and tag their lecture notes
Browse and download notes by subject, course, or teacher
Rate and comment on notes
Earn points or badges for sharing
🔧 Features:
User login
Upload/download notes (PDF, DOCX)
Tag notes with subject, course, semester
Search and filter notes
Rating system (stars or thumbs up)
Admin moderation panel
💥 Why It’s Great:
Encourages collaboration and generosity
Visually engaging with note previews and tags
Easy to gamify (leaderboard for top contributors)


# NoteSwap – Quick Start Guide for Teachers

Welcome to NoteSwap! This guide will help you run the app locally using Docker.

---

## 🚀 Getting Started

### 1. Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) must be installed on your computer.

---

### 2. Download the Project

- Clone or download the NoteSwap project folder to your computer.

---

### 3. Start the Application

Open a terminal in the project folder (where `docker-compose.yml` is located), then run:

```bash
docker compose up --build
```

Wait until you see:
```
Starting development server at http://0.0.0.0:8000/
```

---

### 4. Access the App

- Open your browser and go to: [http://localhost:8000/](http://localhost:8000/notes)

---

### 5. Create an Admin Account (First Time Only)

In a new terminal window, run:

```bash
docker compose exec web python manage.py createsuperuser
```

Follow the prompts to set up your admin username and password.

---

### 6. Login and Use

- Go to [http://localhost:8000/admin/](http://localhost:8000/admin/) to manage users and notes as an admin.
- Teachers and students can register and log in from the main page.

---

### 7. Stopping the App

To stop the app, press `Ctrl+C` in the terminal, then run:

```bash
docker compose down
```

---

## ℹ️ Need Help?

If you need test data or run into issues, contact your
