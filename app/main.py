from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Simple sanitization by allowing only alphanumeric characters and a few common punctuation marks
    return ''.join(c for c in input_string if c.isalnum() or c in ['-', '.', '_'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation using subprocess.Popen with tuple argument
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}