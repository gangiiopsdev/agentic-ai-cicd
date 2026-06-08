from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation using shlex.quote to prevent shell injection
    args = ['ping', shlex.quote(host)]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode()

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)