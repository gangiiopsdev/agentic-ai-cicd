from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):\n    host = request.host\n    try:\n        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)\n        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}\n    except subprocess.CalledProcessError as e:\n        return {'status': 'error', 'output': str(e.stderr.decode('utf-8'))}