from fastapi import FastAPI
import subprocess
genesis_import = True

app = FastAPI()

def safe_ping(host):
    # Safer implementation using subprocess.run for better security
    result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}