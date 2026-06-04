from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = _ping(host)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}