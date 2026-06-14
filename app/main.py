from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(char in allowed_chars for char in host):
        try:
            response = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return response.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e.stderr}'
    else:
        return 'Invalid input'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)