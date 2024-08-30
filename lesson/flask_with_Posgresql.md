# Flask Application with PostgreSQL and CORS

```
Prerequisites
Before running this application, ensure you have the following installed:
1. Python 3.x
2. PostgreSQL
3. Flask
4. Psycopg2 (PostgreSQL adapter for Python)
5. Flask-CORS (for handling CORS)
```

```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

```
pip install Flask
pip install psycopg2-binary
pip install flask-cors
```

```
Database Setup
Database Name: flask_api
User: postgres
Password: 1214
Host: localhost
Port: 543
```

```
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

```

```python
import psycopg2

try:
    conn = psycopg2.connect(database="fast_api",
                            user="postgres",
                            password="1214",
                            host="localhost", port="5432")
    print("Database connected successfully")
except:
    print("Database not connected successfully")

```

```python
@app.route('/')
def hello_world():
    cur = conn.cursor()
    cur.execute('''SELECT * FROM public.user''')
    data = cur.fetchall()
    user_list = []
    for item in data:
        user_list.append({
            'id': item[0],
            'name': item[1],
        })
    return user_list
```

