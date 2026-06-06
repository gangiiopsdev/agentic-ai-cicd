from fastapi import FastAPI, HTTPException
import subprocess
import re

class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's a safe hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or '@' in host:
        raise HTTPException(status_code=400, detail='Invalid hostname')
    result = SafePing.safe_ping(host)
    return {"status": "completed", "result": result}