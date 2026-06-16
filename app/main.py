from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Secure implementation using subprocess.run instead of shell=True
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Call the secure function instead of using shell=True
    return execute_ping(host)