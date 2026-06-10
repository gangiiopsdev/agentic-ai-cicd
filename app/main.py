from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)