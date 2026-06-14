from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run with check=True and capture_output
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)