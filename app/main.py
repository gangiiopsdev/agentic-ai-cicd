from fastapi import FastAPI
import subprocess
git_path = '/usr/bin/git'

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run([git_path, 'ping', sanitized_host], check=True, shell=False)
    return {"status": "completed"}