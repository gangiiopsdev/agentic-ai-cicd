from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str) -> str:
    # Sanitize the input to prevent injection attacks
    try:
        host = shlex.quote(host)
        subprocess.call(['ping', host])
        return {"status": "completed"}
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)