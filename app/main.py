from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize input further to prevent shell injection
    if not host.isalnum():
        return {'status': 'error', 'result': 'Invalid input'}
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result['result']:
        return result
    else:
        return {'status': 'completed', 'result': result}