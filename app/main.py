from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in '.-' for c in host):
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, shell=False)
        if result.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'status': 'failed', 'error': result.stderr}
    except Exception as e:
        return JSONResponse(content={'status': 'failed', 'error': str(e)}, status_code=500)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)