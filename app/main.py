from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping -c 4 {sanitized_host}')
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}