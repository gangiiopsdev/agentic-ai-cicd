from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    is_successful, output = safe_ping(host)
    if is_successful:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}