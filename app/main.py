from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if all(c.isalnum() or c in '-.:/\' for c in host):
        subprocess.call(["ping", host], shell=False)
    else:
        return {"error": "Invalid input"}
    return {"status": "completed"}