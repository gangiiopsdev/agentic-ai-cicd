from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    # Implement proper sanitization logic here
    return input_string

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(["ping", quote(sanitized_host)], check=True)
    return {"status": "completed"}