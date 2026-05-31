from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Simple sanitization example; improve as needed
    return input_str.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):,
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)
    return {"status": "completed"}