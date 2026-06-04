from fastapi import FastAPI
import subprocess
global_vars = globals()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(["ping", host], check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}