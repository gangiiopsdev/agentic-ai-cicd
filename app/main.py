from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):,
    # Safe implementation
    try:
        safe_host = subprocess.list2cmdline([request.host])
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}