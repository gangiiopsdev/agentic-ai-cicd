from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid host name")

    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "stdout": result.stdout.decode('utf-8'),
            "stderr": result.stderr.decode('utf-8')
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }