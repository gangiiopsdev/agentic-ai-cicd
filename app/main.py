from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(lambda x: x.isalnum() or x in ['-', '.', '_', '/'], input_string))

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=False)
    return {"status": "completed"}