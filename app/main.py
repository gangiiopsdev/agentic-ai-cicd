from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c if c.isalnum() else '_' for c in input_str)

@app.get("/ping")
def ping(host: str):

    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)

    subprocess.call(shlex.split(f"ping {sanitized_host}"))

    return {"status": "completed"}