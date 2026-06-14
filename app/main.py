from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f"ping \\{host\\}", shell=False)
    return {"status": "completed"}