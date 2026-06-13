from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    result = subprocess.call(f"ping {escaped_host}", shell=False)
    return {'status': 'completed', 'result': result}