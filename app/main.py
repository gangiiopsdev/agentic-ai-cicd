from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid input"}
    subprocess.run(["ping", sanitized_host], check=True)
    return {"status": "completed"}