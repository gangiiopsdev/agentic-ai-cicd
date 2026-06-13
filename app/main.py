from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}