from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and proper argument parsing
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {'status': 'completed', 'result': result.stdout}