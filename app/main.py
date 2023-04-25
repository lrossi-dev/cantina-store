#!/usr/bin/env python3
import os

from flask import Flask, jsonify, render_template
from flaskext.mysql import MySQL


def create_app(config=None):
    app = Flask(__name__)

    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'Cantina'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    
    mysql = MySQL()
    mysql.init_app(app)

    conn = mysql.connect()

    @app.route("/")
    def buscar_todos_os_lanches():
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Lanches')
        lanches = cursor.fetchall()
        return jsonify(lanches)

    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app = create_app()
    app.run(host="0.0.0.0", port=port)

