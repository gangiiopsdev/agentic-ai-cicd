from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))
    return {"status": "completed"}