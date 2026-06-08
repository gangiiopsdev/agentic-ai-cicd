from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        subprocess.call(['ping', '-c', '1', safe_host])
        return {"status": "completed", "host": host}
    except Exception as e:
        return {"error": str(e), "status": "failed"}