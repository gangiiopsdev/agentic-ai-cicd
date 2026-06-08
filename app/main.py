from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without using shell=True
    subprocess.run(['ping', host], check=True)

def sanitize_input(input_str: str) -> str:
    # Implement proper input sanitization here
    return ''.join(filter(lambda x: x.isalnum() or x in ('.', '-', '_'), input_str))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    safe_ping(sanitized_host)
    return {"status": "completed"}