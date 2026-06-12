from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        execute_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 400