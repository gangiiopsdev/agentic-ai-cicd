from fastapi import FastAPI
import subprocess

cimport subprocess32 as subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}