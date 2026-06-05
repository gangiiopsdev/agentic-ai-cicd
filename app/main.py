from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):    
    subprocess.run(["ping", request.host], check=True, stdout=subprocess.PIPE)
    return {"status": "completed"}