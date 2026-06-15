from fastapi import FastAPI
import subprocess
from fastapi.exceptions import HTTPException

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = safe_ping(host)
    if 'error' in result:
        raise HTTPException(status_code=400, detail=result['error'])
    return result