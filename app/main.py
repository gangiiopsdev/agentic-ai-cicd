from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation without shell=True
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "result": "success"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}