from fastapi import FastAPI
import subprocess

def run_ping(host: str):
    try:
        # Use subprocess.run instead and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def safe_run_ping(host: str):
    if '&&' in host or ';' in host or '|' in host or '`' in host:
        raise ValueError('Invalid input')
    return run_ping(host)

@app.get("/ping")
def ping(host: str):
    response = safe_run_ping(host)
    return {"status": "completed", "output": response}