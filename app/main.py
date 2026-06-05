from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}