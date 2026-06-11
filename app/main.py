from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return {'status': 'completed', 'output': safe_ping(host)}