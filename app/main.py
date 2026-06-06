from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def safe_ping(host: str):
    valid_hosts = ['localhost', '127.0.0.1']
    if host.strip() in valid_hosts or any(host.startswith(ip) for ip in valid_hosts):
        return True
    return False

@app.get("/ping")
def ping(host: str):
    try:
        if safe_ping(host):
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, timeout=5, check=True)
            return JSONResponse(content={'status': result.stdout}, status_code=200)
        else:
            return JSONResponse(content={'error': 'Invalid host'}, status_code=400)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': f'Ping failed: {e.stderr}'}, status_code=400)
    except Exception as e:
        return JSONResponse(content={'error': f'Error pinging {host}: {e}'}, status_code=500)