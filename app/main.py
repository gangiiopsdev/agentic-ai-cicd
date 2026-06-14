from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Simple sanitization example, replace with more robust solution
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.run(args)
    return {"status": "completed"}