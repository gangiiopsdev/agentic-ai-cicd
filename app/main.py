from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.Popen instead of subprocess.call
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    try:
        ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500