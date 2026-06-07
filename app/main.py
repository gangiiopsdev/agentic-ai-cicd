from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Add your input sanitization logic here
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_input(host)\n    subprocess.call(f"ping {sanitized_host}", shell=True)\n    return {"status": "completed"}