from fastapi import FastAPI
import subprocess
def is_safe_hostname(hostname):
    # Basic check for safe hostname characters
    return hostname.isalnum()

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    if is_safe_hostname(request.host):
        subprocess.run(['ping', request.host], check=True, shell=False)
    else:
        return {'status': 'error', 'message': 'Invalid hostname'}
    return {'status': 'completed'}