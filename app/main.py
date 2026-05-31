from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.Popen with shell=False and avoiding shell=True
    try:
        # Validate input to prevent injection attacks
        host = shlex.quote(host)
        subprocess.call(['ping', host])
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}