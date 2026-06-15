from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)