from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Safe implementation using a list of arguments
    subprocess.call(['ping', request.host])
    return {"status": "completed"}