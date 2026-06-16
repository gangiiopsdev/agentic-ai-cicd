from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    safe_host = ''.join(e for e in host if e.isalnum() or e in '-.')
    return 'localhost' if not safe_host else safe_host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', safe_ping(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}