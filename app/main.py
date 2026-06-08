from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed", "output": None}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "output": e.output.decode()}