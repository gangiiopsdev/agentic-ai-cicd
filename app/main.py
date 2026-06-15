from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add your validation logic here, e.g., checking for allowed domains or IP ranges
    return True if host in ['example.com', '127.0.0.1'] else False

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid host"}, 400
    # Secure implementation using subprocess.run with shell=False and argument substitution
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}