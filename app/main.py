from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'success', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if '@' in host or '&' in host or ';' in host or '`' in host:
        return JSONResponse(content={'status': 'failure', 'error': 'Invalid input'}, status_code=400)
    result = safe_ping(host)
    return JSONResponse(content=result)