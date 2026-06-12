from fastapi import FastAPI
import subprocess
global completed = False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if '@' in host or ';' in host:
        return {'error': 'Invalid input'}
    subprocess.run(['ping', host], check=True)
    global completed = True
    return {'status': 'completed'}