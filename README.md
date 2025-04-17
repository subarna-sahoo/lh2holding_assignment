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
git clone https://github.com/your-repo/rss-summarizer.git
cd rss-summarizer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file with the following:
```env
SQLALCHEMY_DATABASE_URI=postgresql://user:password@localhost:5432/rss_db
OPENAI_API_KEY=your_openai_api_key
```

### 3. Initialize Database
```bash
flask db init
flask db migrate
flask db upgrade
```

### 4. Run App
```bash
flask run  # or use main.py
```

---

## 🐳 Docker (Recommended)
```bash
docker-compose up --build
```
Access:
- Flask App: [http://localhost:5000](http://localhost:5000)
- Flower: [http://localhost:5555](http://localhost:5555)

---

## 📊 Features
- Background task queue with Celery + RabbitMQ
- Custom RSS parser support per source
- Summarization via OpenAI
- Article filter via date & source
- Clean Bootstrap UI with AJAX rendering

---

## 🛠 Technologies Used
- Flask / SQLAlchemy / Alembic
- Celery / RabbitMQ / Flower
- OpenAI API
- Bootstrap / Jinja2 / jQuery
- Docker / Docker Compose

---

## ✨ Author
**Your Name**  
GitHub: [@subarna_sahoo](https://github.com/subarna_sahoo)

---

## 📄 License
[MIT](LICENSE)
