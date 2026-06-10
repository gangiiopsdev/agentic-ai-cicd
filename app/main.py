from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    subprocess.call(['ping', shlex.quote(safe_host)])  # Use shlex.quote to sanitize the input
    return {"status": "completed"}