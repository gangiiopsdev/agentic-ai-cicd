from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using parameterized arguments
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)