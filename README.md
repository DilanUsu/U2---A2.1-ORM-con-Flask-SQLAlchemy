# U2 - A2 ORM con Flask-SQLAlchemy

1. Copia `.env.example` a `.env` y pon tu contraseña de MySQL.
2. `mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS juegos CHARACTER SET utf8mb4;"`
3. `pip install -r requirements.txt`
4. Git Bash: `export FLASK_APP=app.py`
5. `flask db init && flask db migrate -m "crear tabla juegos" && flask db upgrade`
6. `flask run`
