# RSS Article Summarizer

A Flask-based web application that fetches and summarizes RSS feed articles using Celery, OpenAI, and PostgreSQL. This project includes background task handling, real-time monitoring via Flower, and article visualization with filtering support.

---

## 📁 Project Structure

```plaintext
.
├── Dockerfile                    # Main Dockerfile for Flask app
├── Dockerfile.flower             # Dockerfile for Flower monitoring UI
├── docker-compose.yaml           # Docker setup for Flask, Celery, RabbitMQ, Flower
├── main.py                       # Entrypoint for running Flask app (if not using Docker)
├── app/
│   ├── __init__.py               # Flask app factory setup
├── models/
│   ├── base.py                   # SQLAlchemy base & DB init
│   ├── article.py                # Article model definition
│   ├── source.py                 # Source model definition
├── routers/
│   ├── articles.py               # Article-related routes & API
│   ├── sources.py                # Source-related routes & API
├── services/
│   ├── parser_factory.py         # RSS parser factory to dispatch by source
│   ├── rss_parser.py             # Orchestration of all RSS feed parsing
│   └── parsers/
│       ├── base.py               # Base parser class
│       ├── air_land_sea_parser.py
│       ├── aviation_parser.py
├── utils/
│   ├── celery_app.py             # Celery app init with Flask context
│   ├── summarizer.py             # OpenAI summary logic
│   ├── tasks.py                  # Celery tasks (fetching/summarizing)
├── templates/
│   └── articles.html             # Jinja2 template with AJAX + Bootstrap
├── migrations/                  # Alembic migration files
├── requirements.txt             # Python dependencies
├── README.md                    # 📘 You're reading it!
```

---

## 🚀 How to Run Locally

### 1. Clone and Setup
```bash
git clone https://github.com/subarna-sahoo/lh2holding_assignment.git
cd lh2holding_assignment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file with the following:
```env
FLASK_ENV=development

# PostgreSQL
POSTGRES_USER=rss_user
POSTGRES_PASSWORD=rss_pass
POSTGRES_DB=rss_data
POSTGRES_DB_URI=postgresql://rss_user:rss_pass@db:5432/rss_data
SQLALCHEMY_DATABASE_URI=postgresql://rss_user:rss_pass@db:5432/rss_data

# Redis
REDIS_URL=redis://redis:6379/0
REDIS_PASSWORD=your_secure_password

# OpenAI
OPENAI_API_KEY=your_openai_api_key

# Celery (RabbitMQ as broker)
CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
CELERY_RESULT_BACKEND=rpc://

```

### 3. Initialize Database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Run App
```bash
flask run  # or use python3 main.py
```

---

## 🐳 Docker (Recommended)
```bash
docker-compose up --build
```
Access:
- Flask App: [http://localhost:5000](http://localhost:5000)
- Flower: [http://localhost:5555](http://localhost:5555)

If you want to manually run DB migration after containers start:
```bash
docker-compose exec flask_app flask db upgrade # can be added as script to run after project starts
```

---

## 📬 Postman Collection
A Postman collection is available for testing the APIs.
- 🌐 [View Postman Collection Online](https://.postman.co/workspace/My-Workspace~46438c75-9823-41c8-886e-c03d33fa4ce5/collection/19852477-3c923ccb-62cd-444d-85b0-a1c56003a465?action=share&creator=19852477)
- 💡 Import it into Postman using **File > Import > Link** or **Upload Files**

---

## 📊 Features
- Background task queue with Celery + RabbitMQ
- Custom RSS parser support per source
- Summarization via OpenAI
- Article filter via date; you can use pagination as well
---

## 🛠 Technologies Used
- Flask / SQLAlchemy / Alembic
- Celery / RabbitMQ / Flower
- OpenAI API
- Bootstrap / Jinja2 / jQuery
- Docker / Docker Compose

---

## 🖼️ UI Preview
Below is a screenshot of the article listing page:
![View Articles UI](https://github.com/user-attachments/assets/26259788-d8cb-47c9-b35e-3139776ba96f)

---
