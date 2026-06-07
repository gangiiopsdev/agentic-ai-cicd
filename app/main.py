from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', request.host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}