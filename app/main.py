from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    host = request.host
    try:
        output = subprocess.check_output(['ping', '-c', '1', '--', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}