from fastapi import FastAPI
import subprocess
git_path = '/usr/bin/ping'  # Specify the full path to ping

app = FastAPI()

def _ping(host):
    try:
        subprocess.run([git_path, host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return _ping(host)