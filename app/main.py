from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def safe_ping(host: str) -> Optional[str]:
    if not host or len(host) > 255:
        return None
    try:
        result = subprocess.run(['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if output is None:
        return {"status": "error", "message": "Invalid host input"}
    return {"status": "completed", "output": output}