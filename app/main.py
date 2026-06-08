from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(host_request: PingRequest):
    host = host_request.host
    # Secure implementation using subprocess.call with shell=False
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}