from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement your sanitization logic here
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char for char in input_string if char in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):
    # Sanitize the input before using it
    sanitized_host = sanitize_input(host)
    subprocess.call(["ping", sanitized_host], shell=False)
    return {"status": "completed"}