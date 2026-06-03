from fastapi import FastAPI
import subprocess
def run_ping(host):
    args = shlex.split('ping')
    args.append(host)
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}