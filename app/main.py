from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def ping(host: str):
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "output": result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "error": e.stderr.decode()}

app = FastAPI()

def ping_host(host: str):
    return SafePing.ping(host)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping_host(host)