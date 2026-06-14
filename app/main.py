from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run for safer execution
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)