from app import app, db, User
from werkzeug.security import generate_password_hash

def seed_user():
    with app.app_context():
        # Create a sample user
        username = "sampleuser"
        password = "samplepassword"
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Add user to the database
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        print(f"User '{username}' added to the database.")

if __name__ == "__main__":
    seed_user()
