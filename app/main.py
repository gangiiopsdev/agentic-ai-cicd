from fastapi import FastAPI
import subprocess
class PingResponse(BaseModel):
    status: str
app = FastAPI()
@app.get("/ping")
def ping(host: str):    # Vulnerable implementation    result = subprocess.run(['ping', host], capture_output=True, text=True)    return PingResponse(status=result.stdout)