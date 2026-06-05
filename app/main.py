from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}