from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    return ''.join(char for char in input_str if char.isalnum() or char in [' ', '-'])

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['/bin/ping', '-c', '1', safe_host], stderr=subprocess.STDOUT)
        return JSONResponse(content={"status": "completed", "output": output.decode()}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": e.output.decode()}, status_code=500)