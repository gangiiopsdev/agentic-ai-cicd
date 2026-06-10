from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(value: str) -> str:
    return ''.join(filter(str.isalnum, value))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    command = shlex.split(f'ping {sanitized_host}')
    subprocess.call(command)
    return {"status": "completed"}