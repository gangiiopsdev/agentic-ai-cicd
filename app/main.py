from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation using subprocess.run and validate input
        if host.strip().isdigit():
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        else:
            raise ValueError('Invalid input for ping host')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)