from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host or host.strip() == '':
        raise ValueError('Invalid host')
    command = f"ping {host}"
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}