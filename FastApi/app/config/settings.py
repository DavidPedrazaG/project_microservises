# settings.py
"""Configuration settings for the application, including database settings."""

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = {
    "name": os.getenv("MYSQL_DATABASE"),
    "engine": "peewee.MySQLDatabase",  # MySQL as the database engine
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "host": os.getenv("MYSQL_HOST"),
    "port": int(os.getenv("MYSQL_PORT")),
}
