from fastapi import FastAPI
import subprocess
def sanitize_input(value: str) -> bool:
    return value.isalnum() or '-' in value

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}