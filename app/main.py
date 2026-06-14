from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if 'ping' not in input_string:
        return None
    return input_string

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host is None:
        return {"status": "error", "message": "Invalid input"}
    result = subprocess.run([sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}