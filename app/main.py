from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    # Use shell=False for security reasons
    result = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
    return result.stdout
class SafePingRequest(BaseModel):
    host: str@app.get("/ping")
def ping(request: SafePingRequest):
    try:
        output = safe_ping(request.host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}