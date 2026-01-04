# Eneba Backend – Internship Assignment

This repository contains the **backend** part of the Eneba Software Engineer Intern assignment.  
The backend is built with **Flask** and uses **SQLite** to store game data.

---

## 🚀 Live Application

If deployed, the backend API base URL is:
```
https://eneba-backend.onrender.com
```

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- Flask-CORS
- Gunicorn
- SQLite3

---

## 🎮 Features

- Stores game data in a SQLite database (`games.db`)
- Returns game list via `/list` endpoint
- Supports search with `search` query parameter (fuzzy matching via `LIKE` in SQL)
- Returns JSON response with total count and list of games

---

## 📦 Database Initialization

The database is initialized automatically when the app runs with `init_db()`:

- Table: `games`
- Columns: `id`, `title`, `aliases`, `old_price`, `new_price`, `discount_pct`, `cashback`, `likes`, `image_url`, `platform`, `region`
- Preloaded with at least 3 required games: FIFA 23, Red Dead Redemption 2, Split Fiction

---

## 🔗 API Endpoints

### GET /list

Returns the list of all games.

Example:
```
GET /list
```

### GET /list?search=<gamename>

Returns games matching the search query in `title` or `aliases`. For example, searching for FIFA:

```
GET /list?search=fifa
```

Response example:
```json
{
  "count": 4,
  "games": [
    {
      "id": 1,
      "title": "EA SPORTS™ FIFA 23 Standard Edition Xbox Series X|S Key GLOBAL",
      "aliases": "fifa23, fifa 23, football",
      "old_price": 79.99,
      "new_price": 25.35,
      "discount_pct": 68,
      "cashback": 2.79,
      "likes": 1817,
      "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/FIFA_23_Cover.jpg/250px-FIFA_23_Cover.jpg",
      "platform": "Xbox Live",
      "region": "Global"
    }
    // 3 more FIFA entries
  ]
}
```

This shows that a search for `fifa` correctly returns **count: 4**.

---

## 🛠️ Running Locally

### Prerequisites
- Python 3.x
- pip

### Install dependencies
```bash
pip install flask flask-cors gunicorn
```

### Run the app
```bash
python app.py
```
The server will run on:
```
http://127.0.0.1:5000
```

The database (`games.db`) is initialized automatically with sample games when the server starts.

---

## 📄 Author

**Stanislovas Albertas Versockis**  
Software Engineer Intern Applicant  
GitHub: https://github.com/whtt1

