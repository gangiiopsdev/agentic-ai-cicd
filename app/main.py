from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.run instead of subprocess.call for better security
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise HTTPException(status_code=400, detail='Invalid hostname')
    result = subprocess.run(['ping', '-c', '1', '--'], capture_output=True, text=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    try:
        response = safe_ping(host)
        return {'status': 'completed', 'response': response}
    except HTTPException as e:
        return {'status': 'error', 'message': e.detail}