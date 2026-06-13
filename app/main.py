from fastapi import FastAPI
import subprocess
def execute_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        execute_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}