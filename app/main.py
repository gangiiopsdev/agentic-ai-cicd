from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value: str) -> str:
    # Basic sanitization example, real-world use should be more robust
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, value))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}