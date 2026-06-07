from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def safe_ping(host):
    if not host:
        return None
    try:
        # Use check_output to avoid shell=True and validate the command input
        result = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'result': result}
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)