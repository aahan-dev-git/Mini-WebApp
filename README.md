# FastAPI Mini Web App (CRUD)

A simple CRUD web application built using FastAPI, HTML, Jinja2 Templates, and JSON file storage.

## Features

- Add a new user
- View all users
- Search users by name
- Delete users
- Store user data in a JSON file

## Tech Stack

- Python
- FastAPI
- Jinja2 Templates
- HTML
- JSON
- Uvicorn

## Project Structure

```
Mini-WebApp/
│
├── main.py
├── users.json
├── templates/
│   ├── index.html
│   ├── users.html
│   └── search.html
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aahan-dev-git/Mini-WebApp.git
```

2. Navigate to the project directory:

```bash
cd Mini-WebApp
```

3. Install the required dependencies:

```bash
pip install fastapi uvicorn jinja2 python-multipart email-validator
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000
```

## Available Routes

| Route | Method | Description |
|------|------|------|
| `/` | GET | Home Page |
| `/search_page` | GET | Search User Page |
| `/search` | GET | Search User by Name |
| `/users` | GET | Display All Users |
| `/submit` | POST | Add a User |
| `/user_delete` | POST | Delete a User |

## Author

- Aahan
