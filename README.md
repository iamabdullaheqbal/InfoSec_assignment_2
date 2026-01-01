# Dictionary Attack Assignment

**Name:** Abdullah  
**Student ID:** 23018020054  
**Course:** Information Security

## Objective
This assignment demonstrates the concept of dictionary attacks by implementing a simple attack against hashed passwords stored in a database.

## Description
The application performs the following steps:
1. User inputs a password, which is hashed using SHA-256 and stored in an SQLite database
2. The script reads a dictionary file (wordlist) and hashes each word
3. If any hash matches the stored hash, the script prints the cracked password
4. If no match is found, it prints "Password not found in dictionary"

## Files Structure
- `main.py` - FastAPI application with endpoints for storing and cracking passwords
- `security.py` - Password hashing functions
- `database.py` - Database configuration and connection
- `models.py` - SQLAlchemy models for the User table
- `attack.py` - Dictionary attack implementation
- `dictionary/wordlist.txt` - Dictionary file containing potential passwords
- `passwords.db` - SQLite database file
- `pyproject.toml` - Project configuration and dependencies (managed by uv)
- `uv.lock` - Lock file with exact dependency versions
- `.venv/` - Virtual environment created by uv

## Installation
1. Make sure you have `uv` installed. If not, install it:
   ```bash
   # On Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Run the application:
   ```bash
   uv run uvicorn main:app --reload
   ```

   Or activate the virtual environment and run:
   ```bash
   # Activate virtual environment
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # macOS/Linux
   
   uvicorn main:app --reload
   ```

## Usage
The application runs on `http://127.0.0.1:8000/docs`

### API Endpoints:
- `POST /store-password/` - Store a hashed password
- `GET /crack-password/` - Perform dictionary attack on the latest stored password

### Example:
1. Store a password: `POST /store-password/?password=hello`
2. Crack the password: `GET /crack-password/`

## Development
This project uses `uv` as the package manager for faster dependency resolution and virtual environment management.

### Adding new dependencies:
```bash
uv add package-name
```

### Running in development mode:
```bash
uvicorn main:app --reload
```
## Security Note
This implementation uses SHA-256 without salt for educational purposes. In production, use proper password hashing libraries like bcrypt or Argon2.