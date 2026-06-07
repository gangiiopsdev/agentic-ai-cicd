from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in valid_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        args = ['ping', host]  # Remove subprocess.quote to avoid command injection
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Invalid host')