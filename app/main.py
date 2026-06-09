from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    cmd = ['ping'] + shlex.split(host)
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "error", "message": str(e)}