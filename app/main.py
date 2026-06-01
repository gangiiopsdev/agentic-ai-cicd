from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

def validate_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid host"}
    sanitized_host = sanitize_input(host)
    subprocess.call(f'ping {sanitized_host}', shell=False)
    return {"status": "completed"}