from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run for a safer approach
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

@app.get("/ping")
def ping(host: str):
    # Using the safe function defined above
    status = safe_ping(host)
    return {'status': 'completed', 'result': status}