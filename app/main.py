from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isalnum():
            return JSONResponse(status_code=400, content={'error': 'Invalid host name'})
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return JSONResponse(content=result.stdout)
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})