from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', ' ', '/'])

@app.get("/ping")
def ping(host: str):

    # Sanitized implementation
    subprocess.call(f"ping {sanitize_input(host)}", shell=False)

    return {"status": "completed"}