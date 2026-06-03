from fastapi import FastAPI
import subprocess
from typing import Any, Dict

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> Dict[str, Any]:
    if not host:
        return {"status": "error", "message": "Host is required"}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.stderr}