from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):  # Use Pydantic model to validate input
    host = request.host
    subprocess.call(f'ping {host}', shell=False)
    return {"status": "completed"}