"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaaide7avj5o490a7qg-a.oregon-postgres.render.com",
        database="todo_tf3n",
        user="todo_tf3n_user",
        password="L5Dyo4S9IXbBr7B8xkF2OhGxt6kntxDq")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
