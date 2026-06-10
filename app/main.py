from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    try:
        response = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "response": response.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}