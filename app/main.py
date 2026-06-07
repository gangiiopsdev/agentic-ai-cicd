from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Call the safe_ping function instead of using subprocess.call with shell=True
    status = safe_ping(host)
    return {"status": "completed", "output": status}