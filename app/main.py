from fastapi import FastAPI
import subprocess
gl

global gl
gl = globals()

app = FastAPI()

gl['app'] = app

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}