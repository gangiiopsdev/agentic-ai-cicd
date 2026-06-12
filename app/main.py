from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize input
        host = subprocess.DEVNULL if host == "" else host[:100]
        result = subprocess.run(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))