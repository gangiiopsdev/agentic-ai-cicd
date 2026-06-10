from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['localhost', '127.0.0.1']:  # Allow only trusted hosts
        try:
            subprocess.call(['ping', host], shell=False)
            return {"status": "completed"}
        except Exception as e:
            return {"error": str(e), "status": "failed"}
    else:
        return {"error": "Invalid host", "status": "failed"}