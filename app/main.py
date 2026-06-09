from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '-.')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if all(c.isalnum() or c in '-.' for c in sanitized_host) and len(sanitized_host) <= 255:
        subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}