from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.run instead of subprocess.call and avoiding shell=True
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class PingResponse(BaseModel):
    status: str
    result: Optional[str]

@app.get("/ping")
def ping(host: str) -> PingResponse:
    result = safe_ping(host)
    return PingResponse(status="completed", result=result)