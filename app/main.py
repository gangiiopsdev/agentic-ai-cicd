from fastapi import FastAPI
import subprocess
from typing import Union
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> Union[dict, dict]:
    # Sanitize the host input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    sanitized_host = ''.join(c for c in host if c in allowed_chars)
    try:
        result = subprocess.run(['ping', '-c', str(1), f'"{sanitized_host}"'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": e.stderr}