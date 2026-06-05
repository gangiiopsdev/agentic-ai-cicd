from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):  # Basic validation of input
        return "Invalid input"
    subprocess.call(f"ping {host}", shell=False)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'status' in result:
        return result
    else:
        return {"message": result}