from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        sanitized_host = ''.join(char for char in host if char.isalnum() or char in ['-', '.'])
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = ''.join(char for char in host if char.isalnum() or char in ['-', '.'])
    result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}