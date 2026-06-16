from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, shell=False, capture_output=True, text=True)
        return {'status': 'success', 'message': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return result