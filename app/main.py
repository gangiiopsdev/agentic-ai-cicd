from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', host], check=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get="/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}