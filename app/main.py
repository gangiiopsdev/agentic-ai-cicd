from fastapi import FastAPI
import subprocess
import shlex
global pids
pids = {}

def start_ping_process(host):
    cmd = 'ping '
    args = shlex.split(cmd + host)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pids[process.pid] = process

def stop_ping_process(pid):
    if pid in pids:
        pids[pid].kill()
        del pids[pid]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post("/ping")
def ping(host: str):
    start_ping_process(host)
    return {"status": "completed"}

@app.delete("/stop")
def stop_all_pings():
    for pid in list(pids.keys()):
        stop_ping_process(pid)
    return {"status": "all pings stopped"}