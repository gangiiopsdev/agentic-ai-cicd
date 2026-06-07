from fastapi import FastAPI
import subprocess

def sanitize_input(input_str: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(allowed_chars.__contains__, input_str))

app = FastAPI()
def ping(host: str):
    sanitized_host = subprocess.quote(sanitize_input(host))  # Use subprocess.quote for safe command construction
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)