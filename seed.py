from app import app, db
from models import User, Admin, Transaction

def seed_users():
    users_data = [
        {"first_name": "John", "last_name": "Doe", "username": "John", "email": "john@example.com", "password": "password1"},
       
    ]

    for user_data in users_data:
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()

def seed_admins():
    admins_data = [
        {"first_name": "Admin", "last_name": "One", "username": "admin1", "email": "admin1@example.com", "password": "adminpassword1"},
        
    ]

    for admin_data in admins_data:
        admin = Admin(**admin_data)
        db.session.add(admin)
        db.session.commit()

def seed_transactions():
    transactions_data = [
        {"username": "John", "description": "deposit", "amount": 100},   
    ]

    for transaction_data in transactions_data:
        user = User.query.filter_by(username=transaction_data["username"]).first()
        if user:
            account = user.accounts[0]  # Assuming a user has one account for simplicity
            transaction = Transaction(account_id=account.id, **transaction_data)
            db.session.add(transaction)
            db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_users()
        seed_admins()
        seed_transactions()

    print("Seed data added successfully.")
