from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation using subprocess.run with shell=False and a list of arguments
    subprocess.run(['ping', request.host], check=True)
    return {'status': 'completed'}