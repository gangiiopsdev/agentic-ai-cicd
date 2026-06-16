from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e) + ' (' + e.stderr.decode() + ')'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}