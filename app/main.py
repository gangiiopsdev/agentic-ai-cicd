from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    sanitized_host = ''.join(c if c.isalnum() else '_' for c in host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get="/ping")
def ping(host: str):
    return secure_ping(host)