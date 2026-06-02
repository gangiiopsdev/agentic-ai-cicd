from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_input(user_input):
    return ' '.join(quote(c) for c in user_input.split())

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', escaped_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.stderr}