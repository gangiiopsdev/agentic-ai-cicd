from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)