from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Ensure the host input does not contain malicious characters
        if any(char in host for char in '<>?*|:"/\\'):
            return {'status': 'failed', 'error': 'Invalid host input'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)