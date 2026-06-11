from fastapi import FastAPI
import subprocess
class PingResponse(BaseModel):
    status: str

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return PingResponse(status=result.stdout)
    except subprocess.CalledProcessError as e:
        return PingResponse(status=e.stderr)