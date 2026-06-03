from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}