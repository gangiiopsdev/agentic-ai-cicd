from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = ['ping'] + shlex.split(host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent OS command injection
    if not host.isalnum() or ' ' in host:
        return {"status": "error", "message": "Invalid input"}
    return ping(host)