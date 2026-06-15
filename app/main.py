from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        args = ['ping', host]
        subprocess.run(args, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}