from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else 'Ping failed'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)