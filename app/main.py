from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host: str):
    # Basic validation: allow only alphanumeric characters and some special characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping_route(host: str):
    if is_valid_host(host):
        subprocess.run(['ping', host], check=True, shell=False)
    else:
        raise ValueError('Invalid host')