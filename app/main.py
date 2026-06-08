from fastapi import FastAPI
import subprocess
import shlex
global_hosts = {'example.com'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in global_hosts:
        try:
            output = subprocess.check_output(shlex.split(f"ping {host}"), stderr=subprocess.STDOUT)
            return {
                "status": "completed",
                "output": output.decode('utf-8')
            }
        except subprocess.CalledProcessError as e:
            return {
                "error": "Ping failed",
                "output": e.output.decode('utf-8')
            }
    else:
        return {"error": "Host not allowed"}