from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(c for c in host if c in allowed_chars)
    return sanitized
def validate_input(input_str: str) -> bool:
    # Add more sophisticated validation logic here
    return all(char in allowed_chars for char in input_str)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if validate_input(host):
        command = ['ping', sanitize_host(host)]
        subprocess.call(command)
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}