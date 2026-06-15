from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Use a whitelist of allowed hosts or validate the input
        if request.host not in ['example.com', 'example.org']:
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', request.host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}