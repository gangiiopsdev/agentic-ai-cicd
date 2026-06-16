from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join([char for char in input_string if char in allowed_chars])

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.run(['ping', host], check=True, capture_output=True, text=True, timeout=5)
    return {'status': 'completed', 'output': sanitized_host.stdout}