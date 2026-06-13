from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation using check_output with shell=False and safe argument handling
    try:
        subprocess.check_call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}