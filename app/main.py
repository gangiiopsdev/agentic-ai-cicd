from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    return {'status': 'completed', 'output': safe_ping(host)}