from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        # Use subprocess.run with check=True to handle errors gracefully
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error pinging {host}: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)