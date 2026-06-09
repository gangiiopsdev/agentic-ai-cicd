from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        args = ['ping', host]
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(shlex.quote(host))
    return {'status': 'completed', 'result': result}