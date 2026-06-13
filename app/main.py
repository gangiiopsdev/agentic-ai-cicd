from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate host to ensure it's a valid IP or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host')
        response = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return response.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get('/ping')
def ping(host: str): 
    return {'status': safe_ping(host)}