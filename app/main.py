from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    output = safe_ping(host)
    return {"status": "completed", "output": output}