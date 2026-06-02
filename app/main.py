from fastapi import FastAPI
import subprocess
class PingRequest:
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Safe implementation
    try:
        output = subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}