from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(host: str = Depends(PingRequest)):
    subprocess.call(["ping", host])
    return {"status": "completed"}