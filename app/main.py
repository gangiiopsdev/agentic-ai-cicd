from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    sanitized_host = sanitize_input(host)
    command = ["ping", sanitized_host]
    subprocess.run(command, check=True, shell=False)  # Ensure shell is False to prevent shell injection

    return {"status": "completed"}