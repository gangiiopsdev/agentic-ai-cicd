from fastapi import FastAPI
import subprocess
def escape_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' 
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(['ping', escaped_host], shell=False)
    return {"status": "completed"}