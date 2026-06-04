from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        args = ['ping', host]
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)