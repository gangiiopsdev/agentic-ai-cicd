from fastapi import FastAPI
import subprocess

def run_ping(host: str):
    try:
        # Use subprocess.run instead and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = run_ping(host)
    return {"status": "completed", "output": response}