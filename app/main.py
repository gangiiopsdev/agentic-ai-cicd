from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping'] + shlex.split(host), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)