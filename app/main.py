from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_route(host: str):
    result = ping(host)
    return {'status': 'completed', 'output': result.stdout.decode()}