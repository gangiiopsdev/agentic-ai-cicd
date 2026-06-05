from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if 'localhost' in host or '127.0.0.1' in host or '::1' in host:
        try:
            result = _ping(host)
            return {"status": "completed", "output": result}
        except Exception as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host"}