from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host: str):
    cmd = ['ping', host]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = run_ping(host)
    return {"status": "completed", "response": response}