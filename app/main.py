from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def safe_ping(host: str):
    if host == 'localhost' or host.startswith('192.168.') or host.startswith('172.'):  # Add more allowed hosts as needed
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        return 'Invalid host'

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return JSONResponse(content={"status": "completed", "result": result}, status_code=200)