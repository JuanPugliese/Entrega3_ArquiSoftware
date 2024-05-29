# app/config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mi_usuario:123456789@localhost/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
