# 🎙️ Late Night Show API

A RESTful Flask API for managing a fictional Late Night Show, including users, guests, episodes, and guest appearances. Built with PostgreSQL, SQLAlchemy, Flask-JWT-Extended, and Flask-Migrate.

---

## 📁 Project Structure

late-night-show-api-challenge/
├── server/
│ ├── app.py # Flask app factory
│ ├── config.py # Configuration settings
│ ├── extensions.py # DB, Migrate, JWT initializations
│ ├── models/
│ │ ├── user.py
│ │ ├── guest.py
│ │ ├── episode.py
│ │ └── appearance.py
│ ├── controllers/
│ │ ├── auth_controller.py
│ │ ├── guest_controller.py
│ │ ├── episode_controller.py
│ │ └── appearance_controller.py
│ └── seed.py # Seed data for development
├── migrations/ # Auto-generated DB migration files
├── .env # Environment variables
└── README.md # This file

yaml
Copy
Edit

---

## 🚀 Features

- **JWT Authentication** for secure endpoints
- **CRUD** for Guests, Episodes, Appearances
- **Blueprints** for modular routing
- **PostgreSQL + SQLAlchemy** for relational data modeling
- **Database migrations** using Flask-Migrate

---

## 🧪 Tech Stack

| Technology      | Use                                  |
|----------------|---------------------------------------|
| Flask           | Web Framework                        |
| Flask-JWT-Extended | JWT Authentication              |
| SQLAlchemy      | ORM for DB Models                    |
| PostgreSQL      | Database                             |
| Flask-Migrate   | Alembic-based Migrations             |

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/late-night-show-api-challenge.git
cd late-night-show-api-challenge
2. Create and activate virtual environment
bash
Copy
Edit
python3 -m venv myenv
source myenv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Create PostgreSQL database
Make sure PostgreSQL is running, then:

bash
Copy
Edit
createdb late_show_db
⚠️ If you get a role error like role "your-username" does not exist, create it using:
createuser your-username --superuser

5. Configure environment
Edit .env or server/config.py:

python
Copy
Edit
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:yourpassword@localhost:5432/late_show_db"
JWT_SECRET_KEY = "super-secret"
6. Run migrations
bash
Copy
Edit
export FLASK_APP=server.app:create_app
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
7. Seed the database
bash
Copy
Edit
PYTHONPATH=. python server/seed.py
8. Start the server
bash
Copy
Edit
python server/app.py
Server runs on: http://127.0.0.1:5000

📡 API Endpoints
🔐 Auth
METHOD	ENDPOINT	DESCRIPTION
POST	/login	User login (returns JWT)

🎭 Guests
METHOD	ENDPOINT	DESCRIPTION
GET	/guests	Get all guests
POST	/guests	Create a new guest
PATCH	/guests/<id>	Update guest
DELETE	/guests/<id>	Delete guest

🎬 Episodes
METHOD	ENDPOINT	DESCRIPTION
GET	/episodes	List all episodes
POST	/episodes	Add a new episode

🤝 Appearances
METHOD	ENDPOINT	DESCRIPTION
GET	/appearances	List all guest appearances
POST	/appearances	Create an appearance

🧪 Example Response
GET /guests
json
Copy
Edit
[
  {
    "id": 1,
    "name": "Emma Stone",
    "occupation": "Actor"
  },
  {
    "id": 2,
    "name": "Trevor Noah",
    "occupation": "Comedian"
  }
]
✅ To Do / Improvements
 Add PATCH and DELETE routes for all models

 Add user registration route

 Protect routes using @jwt_required

 Add pagination for large datasets

 Write tests (pytest/unittest)

🧑‍💻 Author
Built with 💻 by [Maitai]

