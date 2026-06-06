from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(char for char in user_input if char.isalnum() or char in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):

    # Sanitize input
    sanitized_host = sanitize_input(host)

    # Vulnerable implementation fixed
    subprocess.call(f"ping {sanitized_host}")

    return {"status": "completed"}