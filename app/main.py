from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from datetime import timedelta

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest, background_tasks: BackgroundTasks):
    try:
        output = subprocess.check_output(['ping', '-c 1', request.host], stderr=subprocess.STDOUT, timeout=timedelta(seconds=5), shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}
    except Exception as e:
        return {'status': 'error', 'output': str(e)}