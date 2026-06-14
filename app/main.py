from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping_route(request: PingRequest):
    host = request.host
    try:
        # Sanitize input to prevent command injection
        if not host.isalnum():
            raise ValueError('Invalid host name')
        response = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': response.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}