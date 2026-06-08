from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
cmd = ['ping', host]
result = subprocess.run(cmd, check=True, capture_output=True, text=True)
return result.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': 'Pinging ' + host}