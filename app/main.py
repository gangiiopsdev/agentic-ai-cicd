from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char in (' ', '-', '.'))

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)  # Improved input sanitization
    subprocess.call(["ping", safe_host], shell=False)
    return {"status": "completed"}