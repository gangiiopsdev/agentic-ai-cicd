from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"error": "Invalid input"}
    # Ensure the host is properly sanitized before using it in the subprocess call
    if any(char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for char in host):
        return {"error": "Invalid input"}
    return safe_ping(host)