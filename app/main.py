from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Basic sanitization, can be more complex based on requirements
    return ''.join(char for char in input_str if char.isalnum() or char in '-.
')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)
    return {"status": "completed"}