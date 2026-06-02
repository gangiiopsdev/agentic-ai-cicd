from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {"status": "completed", "output": response}
    except Exception as e:
        return {"status": "error", "message": str(e)}