from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate the host to prevent command injection
        if not host.strip() or 'localhost' in host or host.startswith('127.0.0.1'):
            result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5, check=True)
            return JSONResponse(content={'status': result.stdout}, status_code=200)
        else:
            return JSONResponse(content={'error': 'Invalid host'}, status_code=400)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': f'Ping failed: {e.stderr}'}, status_code=400)
    except Exception as e:
        return JSONResponse(content={'error': f'Error pinging {host}: {e}'}, status_code=500)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)