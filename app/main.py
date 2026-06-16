from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.quote(host)
    args = shlex.split(f'ping {safe_host}')
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "stdout": result.stdout.decode('utf-8'),
            "stderr": result.stderr.decode('utf-8')
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }