from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['google.com', 'example.com']:  # Add allowed hosts here
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}