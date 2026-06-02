from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(user_input):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(filter(lambda x: x in allowed_chars, user_input))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(shlex.split(f"ping {sanitized_host}"), shell=False)
    return {"status": "completed"}