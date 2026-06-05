from fastapi import FastAPI
import subprocess
def sanitize_input(value):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in value if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):    
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}