from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run for better control and error handling
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return JSONResponse(content={'host': host, 'output': result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'host': host, 'error': str(e)}, status_code=500)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)