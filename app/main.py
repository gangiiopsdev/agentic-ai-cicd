from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}