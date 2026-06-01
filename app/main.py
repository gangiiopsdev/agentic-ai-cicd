from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(char for char in host if char.isalnum() or char in '._-')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    # Secure implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}