from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        command = ['ping'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=10)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    result = safe_ping(host)
    return {"status": "completed", "result": result}