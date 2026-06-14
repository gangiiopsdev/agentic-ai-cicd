from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return \
        ''.join(
            char if char in allowed_chars else ' '
            for char in user_input
        )

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if ' ' in sanitized_host:
        return {"error": "Invalid host", "status": "failed"}
    try:
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"error": str(e), "status": "failed"}