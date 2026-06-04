from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use shell=False and provide a full path for the executable to mitigate command injection risks.
        subprocess.run(['/bin/ping', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)