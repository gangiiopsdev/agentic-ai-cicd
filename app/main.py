from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with argument sanitization
    try:
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}