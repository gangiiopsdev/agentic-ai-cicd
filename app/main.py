from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': e}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)