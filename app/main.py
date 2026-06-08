from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() and e.isdigit())
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid input"}
    subprocess.run(shlex.split(f'ping -c 4 {shlex.quote(host)}'), check=True, text=True)
    return {"status": "completed"}