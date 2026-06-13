from fastapi import FastAPI
import subprocess
def ping(host):
    # Secure implementation
    subprocess.run(['ping', host], check=True, capture_output=True)
app = FastAPI()
class PingRequest(BaseModel):
    host: str
@app.get("/ping")
def ping_endpoint(request: PingRequest):