from fastapi import FastAPI
import subprocess
global hosts_blacklist = set(['example.com', 'test.com'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in hosts_blacklist:
        return {"status": "denied", "reason": "Host is blacklisted"}
    subprocess.call(f'ping {host}', shell=False)
    return {"status": "completed"}