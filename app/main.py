from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest): # Use Pydantic model to validate input
    try:
        result = subprocess.Popen(['ping', request.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
        output, error = result.communicate()
        if result.returncode != 0:
            return {"status": "failed", "error": error}
        else:
            return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}