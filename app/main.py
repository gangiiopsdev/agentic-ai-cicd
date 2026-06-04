from fastapi import FastAPI
import subprocess
import shlex
from fastapi import HTTPException

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run([shlex.quote('ping'), shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))