from fastapi import FastAPI
import subprocess
import shlex

global_args = ['ping']
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with sanitized input
    try:
        args = global_args + [shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}