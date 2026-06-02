from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', ' ', '/'])

@app.get("/ping")
def ping(host: str):

    # Sanitize the input
    host = sanitize_input(host)

    # Safe implementation
    subprocess.call(f"ping {host}", shell=False)

    return {"status": "completed"}