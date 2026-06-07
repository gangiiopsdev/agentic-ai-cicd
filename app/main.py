from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call and avoiding shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Using a safe function to execute the command
    output = safe_ping(host)
    return {"status": "completed", "output": output}