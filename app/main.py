from fastapi import FastAPI
import subprocess
class PingResponse(BaseModel):
    status: str

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> PingResponse:
    # Safe implementation
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return PingResponse(status="completed with output: " + output.stdout)
    except subprocess.CalledProcessError as e:
        return PingResponse(status="failed with error: " + str(e))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}