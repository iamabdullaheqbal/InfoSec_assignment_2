"""
Name: Abdullah
Student ID: 23018020054
Course: Information Security

Assignment: Dictionary Attack Implementation
Objective: The objective of this assignment is to help students understand the concept 
of dictionary attacks by implementing a simple attack against hashed passwords stored in database.

Task Description:
1. User inputs a password, which is hashed and stored in an SQLite database
2. The script then reads a dictionary file (wordlist) and hashes each word
3. If any hash matches the stored hash, the script prints the cracked password
4. If no match is found, it prints "Password not found in dictionary"

Implementation: Dictionary Attack using FastAPI and SQLite
"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Base, User
from security import hash_password
from attack import dictionary_attack

app = FastAPI(title="Dictionary Attack")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/store-password/")
def store_password(password: str, db: Session = Depends(get_db)):
    """Store a hashed password in the database"""
    # Input validation
    if not password or len(password.strip()) == 0:
        return {"error": "Password cannot be empty"}
    
    if len(password) < 1:
        return {"error": "Password must be at least 1 character long"}
    
    try:
        hashed = hash_password(password)
        user = User(password_hash=hashed)
        db.add(user)
        db.commit()
        
        
        
        return {"message": "Password stored successfully", "hash": hashed}
    except Exception as e:
        db.rollback()
        return {"error": f"Failed to store password: {str(e)}"}

@app.get("/crack-password/")
def crack_password(db: Session = Depends(get_db)):
    """Perform dictionary attack on the most recently stored password"""
    try:
        user = db.query(User).order_by(User.id.desc()).first()

        if not user:
            return {"error": "No password stored in database"}

        print(f"Attempting to crack hash: {user.password_hash}")
        cracked = dictionary_attack(user.password_hash)

        if cracked:
            return {"status": "success", "message": "Password cracked", "password": cracked}
        else:
            return {"status": "failed", "message": "Password not found in dictionary"}
    
    except Exception as e:
        return {"error": f"Failed to crack password: {str(e)}"}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8000,
        reload=True
    )

