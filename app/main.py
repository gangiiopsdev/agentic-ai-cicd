from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(char for char in host if char.isalnum() or char in '._-')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    # Secure implementation
    subprocess.run(['ping', '-c 1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}