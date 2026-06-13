from fastapi import FastAPI
import subprocess
global_blacklist = ['ping']

app = FastAPI()
def ping(host: str):
    if host not in global_blacklist:
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Ping is not allowed'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)