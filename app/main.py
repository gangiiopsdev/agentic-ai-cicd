from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(value):
    return shlex.quote(value)

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with sanitized input
    subprocess.run(['ping', sanitize_input(host)], check=True)
    return {"status": "completed"}