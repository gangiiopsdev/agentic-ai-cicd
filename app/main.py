from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', ' ', ':'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = shlex.split(f"ping {sanitized_host}")
    subprocess.run(command, check=True)
    return {"status": "completed"}