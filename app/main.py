from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate host to prevent shell injection
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_host(host: str):
    return ping(host)