from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host input to ensure it does not contain malicious characters
        if not validate_host(host):
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
def validate_host(host: str) -> bool:
    # Simple validation example
    return host.isalnum() and '.' in host