from flaskblog import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
