from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:  # Example of input validation
        return JSONResponse(status_code=400, content={"status": "failed", "error": "Invalid host"})
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return JSONResponse(status_code=400, content={'status': 'failed', 'error': str(e)})