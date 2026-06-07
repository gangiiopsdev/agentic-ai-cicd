from fastapi import FastAPI
import subprocess
import shlex

class PingRequest(BaseModel):
    host: str = Field(..., regex='^(localhost|127\.0\.0\.1)$')

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    args = shlex.split(f'ping {request.host}')
    subprocess.call(args)
    return {"status": "completed"}