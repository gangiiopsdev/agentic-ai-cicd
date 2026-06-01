from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(filter(lambda x: x in allowed_chars, user_input))
    return sanitized

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)
    return {"status": "completed"}