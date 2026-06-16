from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_/')
    return ''.join(filter(allowed_chars.__contains__, input_str))
def validate_host(host):
    # Add validation logic here, e.g., whitelist of allowed hosts
    return host in ['example.com', 'localhost']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', '-c 1', sanitized_host], check=True, shell=False)
    return {'status': 'completed'}