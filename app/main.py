from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = run_ping(shlex.quote(host))
    return {"status": "completed", "output": output}