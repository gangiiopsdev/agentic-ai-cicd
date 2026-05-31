from fastapi import FastAPI
import subprocess
from typing import Union

cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> Union[dict, dict]:
    # Validate the host input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid host input")
    try:
        result = subprocess.run(['ping', '-c', str(1), f'"{host}"'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": e.stderr}