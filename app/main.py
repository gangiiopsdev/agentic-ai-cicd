from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_input(user_input):
    return ' '.join(quote(c) for c in user_input.split())

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    subprocess.run(['ping', escaped_host], check=True)
    return {"status": "completed"}