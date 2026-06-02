from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '--', host]
    subprocess.run(args, check=True, capture_output=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        SafePing.safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}