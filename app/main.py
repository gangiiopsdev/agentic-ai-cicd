from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host and all(char.isalnum() or char in ('.', '-') for char in host):
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Ping failed: {e.stderr}')
    else:
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'result': response}