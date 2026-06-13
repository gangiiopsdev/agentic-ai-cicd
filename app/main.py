from fastapi import FastAPI, Request
import subprocess

class PingResponse(BaseModel):
    status: str

app = FastAPI()

@app.get("/ping")
def ping(request: Request, host: str):    # Fixed implementation
    safe_host = ''.join(e for e in host if e.isalnum() or e in [ '.', '-', '_' ])
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return PingResponse(status=result.stdout)