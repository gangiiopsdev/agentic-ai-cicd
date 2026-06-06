from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    try:
        response = subprocess.run(['ping', request.host], capture_output=True, text=True, timeout=5, shell=False)
        return {'status': 'completed', 'output': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except TimeoutExpired as e:
        return {'status': 'error', 'message': str(e)}