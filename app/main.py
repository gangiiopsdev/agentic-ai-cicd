from fastapi import FastAPI
import subprocess
def secure_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    success, output = secure_ping(host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}