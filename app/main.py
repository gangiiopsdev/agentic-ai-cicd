from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation using subprocess.Popen with a list of arguments and shell=False to avoid command injection
    subprocess.Popen(['ping', request.host], shell=False)
    return {"status": "completed"}