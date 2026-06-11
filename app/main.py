from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    cmd = ["ping", *shlex.split(sanitized_host)]
    subprocess.run(cmd, check=True)
    return {"status": "completed"}