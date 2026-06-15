from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    output = safe_ping(host)
    return {"status": "completed", "output": output}