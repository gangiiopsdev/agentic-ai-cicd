from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    host = request.host\n    # Secure implementation\n    try:\n        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)\n        return {"status": "completed", "output": output}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}