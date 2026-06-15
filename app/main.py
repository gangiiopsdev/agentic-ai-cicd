from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safer implementation using subprocess.run without shell=True
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "error", "output": output}