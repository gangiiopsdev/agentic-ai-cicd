from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.call(args)
    return result

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = safe_ping(host)
        if result == 0:
            return {"status": "completed", "result": "Success"}
        else:
            return {"status": "failed", "result": "Failure"}
    except Exception as e:
        return {"error": str(e)"