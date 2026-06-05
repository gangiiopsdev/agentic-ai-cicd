from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.run instead of subprocess.call for better security
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get="/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}