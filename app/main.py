from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
    return ''.join(char for char in input_str if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    host = sanitize_input(host)
    args = ['ping', shlex.quote(host)]  # Use shlex.quote to safely handle user input
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}