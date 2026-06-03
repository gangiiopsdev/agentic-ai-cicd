from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Simple sanitization example: remove non-alphanumeric characters
    return ''.join(e for e in input_string if e.isalnum() or e == '.')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f"ping {sanitized_host}")
    subprocess.call(args)

    return {"status": "completed"}