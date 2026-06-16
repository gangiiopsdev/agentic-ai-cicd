from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500