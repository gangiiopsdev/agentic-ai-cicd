from fastapi import FastAPI
import subprocess
class Sanitizer:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    @staticmethod
def sanitize_input(user_input):
        return ''.join(char for char in user_input if char in Sanitizer.allowed_chars)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = Sanitizer.sanitize_input(host)
    result = subprocess.run(["ping", sanitized_host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}