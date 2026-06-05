from fastapi import FastAPI
import subprocess
from sanic.response import text

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True, output.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, result = safe_ping(host)
    if success:
        return text(result)
    else:
        return text(result, status_code=500)