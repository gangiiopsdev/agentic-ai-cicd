from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_input(user_input):
    return ''.join(c for c in user_input if c.isalnum() or c in ['-', '.', '_', ' ', '/'])

@app.get("/ping")
def ping(host: str):
    host = escape_input(host)
    subprocess.call(['ping', host])
    return {"status": "completed"}