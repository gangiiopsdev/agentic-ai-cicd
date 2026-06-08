from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return run_ping(host)