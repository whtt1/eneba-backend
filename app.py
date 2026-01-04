from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


def get_db_connection():
    conn = sqlite3.connect('games.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute('DROP TABLE IF EXISTS games')
    conn.execute('''
        CREATE TABLE games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            aliases TEXT,
            old_price REAL,
            new_price REAL NOT NULL,
            discount_pct INTEGER,
            cashback REAL,
            likes INTEGER,
            image_url TEXT,
            platform TEXT,
            region TEXT
        )
    ''')

    games = [
        ('EA SPORTS™ FIFA 23 Standard Edition Xbox Series X|S Key GLOBAL', 'fifa23, fifa 23, football', 79.99, 25.35,
         68, 2.79, 1817,
         'https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/FIFA_23_Cover.jpg/250px-FIFA_23_Cover.jpg',
         'Xbox Live', 'Global'),
        ('EA SPORTS™ FIFA 23 Standard Edition Xbox One Key GLOBAL', 'fifa23, fifa 23, football', 69.99, 22.80, 67, 2.51,
         2799,
         'https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/FIFA_23_Cover.jpg/250px-FIFA_23_Cover.jpg',
         'Xbox Live', 'Global'),
        ('EA SPORTS™ FIFA 23 Standard Edition Xbox Series X|S Key EUROPE', 'fifa23, fifa 23, football', 79.99, 25.88,
         68, 2.85, 1010,
         'https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/FIFA_23_Cover.jpg/250px-FIFA_23_Cover.jpg',
         'Xbox Live', 'Europe'),
        ('EA SPORTS™ FIFA 23 Ultimate Edition Xbox One & Xbox Series X|S Key EUROPE', 'fifa23, fifa 23, football',
         99.99, 42.47, 58, 4.67, 298,
         'https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/FIFA_23_Cover.jpg/250px-FIFA_23_Cover.jpg',
         'Xbox Live', 'Europe'),
        ('Red Dead Redemption 2 PC Rockstar Key GLOBAL', 'rdr2, rdr 2, red dead, redemption', 59.99, 11.96, 80, 1.32,
         25375,
         'https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg', 'Rockstar Games Launcher',
         'Global'),
        ('Red Dead Redemption 2: Ultimate Edition Rockstar Games Launcher Key GLOBAL',
         'rdr2, rdr 2, red dead, redemption', 99.99, 15.30, 85, 1.68, 6840,
         'https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg', 'Rockstar Games Launcher',
         'Global'),
        ('Red Dead Redemption 2: Ultimate Edition (PC) Rockstar Games Launcher Key EUROPE',
         'rdr2, rdr 2, red dead, redemption', 99.99, 15.69, 84, 1.73,
         1116,
         'https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg', 'Rockstar Games Launcher',
         'Europe'),
        ('Red Dead Redemption 2 (PC) Rockstar Games Launcher Key EUROPE', 'rdr2, rdr 2, red dead, redemption', 59.99,
         11.94, 80, 1.31, 2283,
         'https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg', 'Rockstar Games Launcher',
         'Europe'),
        ('Split Fiction EA App Key (PC) GLOBAL', 'sf, splitfiction', 49.99, 40.93, 18, 4.50, 626,
         'https://image.api.playstation.com/vulcan/ap/rnd/202411/2918/90ad70c1ef581f93454184750cba9e0ca37bc7e30a4d1f55.png',
         'EA App', 'Global'),
        ('Split Fiction (Xbox Series X|S) XBOX LIVE Key EUROPE', 'sf, splitfiction', 49.99, 34.14, 32, 3.76, 500,
         'https://image.api.playstation.com/vulcan/ap/rnd/202411/2918/90ad70c1ef581f93454184750cba9e0ca37bc7e30a4d1f55.png',
         'Xbox Live', 'Europe'),
        ('Split Fiction (Xbox Series X|S) XBOX LIVE Key GLOBAL', 'sf, splitfiction', 49.99, 35.15, 30, 3.87, 1039,
         'https://image.api.playstation.com/vulcan/ap/rnd/202411/2918/90ad70c1ef581f93454184750cba9e0ca37bc7e30a4d1f55.png',
         'Xbox Live', 'Global'),
        ('Split Fiction (Nintendo Switch 2) eShop Key EUROPE', 'sf, splitfiction', None, 36.25, 0, 3.99, 288,
         'https://image.api.playstation.com/vulcan/ap/rnd/202411/2918/90ad70c1ef581f93454184750cba9e0ca37bc7e30a4d1f55.png',
         'Nintendo', 'Europe'),
    ]
    conn.executemany('''INSERT INTO games 
        (title, aliases, old_price, new_price, discount_pct, cashback, likes, image_url, platform, region) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', games)
    conn.commit()
    conn.close()


@app.route('/list', methods=['GET'])
def list_games():
    search_query = request.args.get('search', '')
    conn = get_db_connection()
    if search_query:
        query = "SELECT * FROM games WHERE title LIKE ? OR aliases LIKE ?"
        term = f'%{search_query}%'
        games = conn.execute(query, (term, term)).fetchall()
    else:
        games = conn.execute('SELECT * FROM games').fetchall()
    conn.close()

    results = [dict(g) for g in games]
    return jsonify({"count": len(results), "games": results})


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
