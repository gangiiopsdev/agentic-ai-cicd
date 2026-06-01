from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', escape_host(host)]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}