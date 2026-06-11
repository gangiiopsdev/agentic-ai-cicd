from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'success', 'output': output.stdout})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failure', 'error': str(e)}, status_code=500)