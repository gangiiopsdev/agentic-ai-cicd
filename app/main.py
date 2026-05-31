from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not all(c.isalnum() or c in ('.', ':') for c in host):
            raise ValueError("Invalid host input")
        result = subprocess.run(['ping', subprocess.check_output(['echo', host]).decode().strip()], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": e.stderr}