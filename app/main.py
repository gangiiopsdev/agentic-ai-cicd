from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(user_input):
    # Add your validation logic here, e.g., using a whitelist of allowed characters
    return ''.join(char for char in user_input if char.isalnum() or char in [".", ":", "-"])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ["ping", sanitized_host]
    subprocess.call(command)
    return {"status": "completed"}