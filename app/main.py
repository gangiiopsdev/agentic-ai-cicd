from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(sanitize_input(host))
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}