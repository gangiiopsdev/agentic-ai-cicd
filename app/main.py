from fastapi import FastAPI
import subprocess
from fastapi.params import Query

app = FastAPI()

@app.get("/ping")
def ping(host: str = Query(..., min_length=1, regex='^[a-zA-Z0-9.-]+$')):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}