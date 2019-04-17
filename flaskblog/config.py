import os


class Config:
    SECRET_KEY = "akjsgdo3w789123gf9726q3g"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "admin@admin.com"
    MAIL_PASSWORD = "admin"
