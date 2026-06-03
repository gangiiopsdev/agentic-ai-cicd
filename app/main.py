from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}