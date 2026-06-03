from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, str):
        return JSONResponse(content={"status": "completed", "result": result}, status_code=200)
    else:
        return JSONResponse(content={"error": result}, status_code=500)