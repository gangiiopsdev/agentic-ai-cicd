from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isdigit():
        return False
    args = ['ping', '-c', '4', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode(), result.stderr.decode()

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    if not output:
        return {'error': error}
    return {'status': 'completed', 'output': output}