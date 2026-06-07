from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Ensure host is a valid IP or hostname before passing to subprocess
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 400