from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Simple sanitization example; replace with more secure method
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_str if c in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use subprocess.run with shell=False and check=True to avoid command injection
    subprocess.run(['ping', sanitized_host], check=True, shell=False)
    return {'status': 'completed'}