from fastapi import FastAPI
import subprocess
import shlex
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    args = shlex.split(f'ping -c 4 {shlex.quote(host)}')  # Limit the number of pings to avoid abuse
    ping_process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = ping_process.communicate()
    return {
        "status": "completed",
        "output": output.decode('utf-8'),
        "error": error.decode('utf-8')
    }