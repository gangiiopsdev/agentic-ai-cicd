from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent injection attacks
    if not validate_host(host):
        return JSONResponse(status_code=400, content={'error': 'Invalid host'})

    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={'error': f'Ping failed with error: {e.stderr}'})

# Example validation function (implement according to your requirements)
def validate_host(host: str) -> bool:
    # Basic example: only allow alphanumeric characters and hyphens
    return host.isalnum() or '-' in host