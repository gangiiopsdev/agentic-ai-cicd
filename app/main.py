from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': str(e)}, status_code=500)