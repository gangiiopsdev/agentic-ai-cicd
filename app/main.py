from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    # Regex to allow alphanumeric characters, hyphens, and periods
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return JSONResponse(status_code=400, content={"error": "Invalid host"})

    try:
        result = subprocess.run(['ping', f'\\{host}'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={'error': f'Ping failed with error: {e.stderr}'})