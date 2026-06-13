from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['google.com', 'bing.com']:
        args = ['ping', host]
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'success', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failure', 'error': e.stderr.decode()}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host not in ['google.com', 'bing.com']:
        return {'status': 'not allowed'}