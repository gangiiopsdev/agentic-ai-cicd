from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        # Using subprocess.run for safer execution
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)