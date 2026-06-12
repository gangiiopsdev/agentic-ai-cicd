from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str
def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    response = execute_ping(request.host)
    return {"status": "completed", "response": response}