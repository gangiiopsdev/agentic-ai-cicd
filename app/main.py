from fastapi import FastAPI
import subprocess
c from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout.decode('utf-8')}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': e.stderr.decode('utf-8')}, status_code=500)