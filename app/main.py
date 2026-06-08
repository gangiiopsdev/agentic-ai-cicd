from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in '._-')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.call([quote('ping'), quote(sanitized_host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

# Preventive Controls:
# 1. Use parameterized queries or prepared statements for database operations.
# 2. Validate and sanitize all user inputs before using them in commands.
# 3. Avoid running untrusted code with elevated privileges.