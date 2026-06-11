from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_string):
    # Implement proper sanitization logic here
    return input_string

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(["ping", quote(sanitized_host)], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}

# Additional validation and sanitization of input can be added here.