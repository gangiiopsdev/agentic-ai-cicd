from fastapi import FastAPI
import subprocess
from fastapi.responses import HTTPException

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ping")
def ping_route(host: str):
    return ping(host)