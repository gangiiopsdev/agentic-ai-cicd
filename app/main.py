from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(user_input):
    return shlex.quote(user_input)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input sanitization
    sanitized_host = sanitize_input(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}