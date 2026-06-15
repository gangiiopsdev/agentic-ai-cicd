from fastapi import FastAPI
import subprocess
globally_allowed_hosts = ['example.com', 'another-example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in globally_allowed_hosts:
        return {"error": "Host is not allowed"}, 403

    # Safe implementation
    subprocess.call(f'ping {host}', shell=False)

    return {"status": "completed"}