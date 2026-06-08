from fastapi import FastAPI
import re
import subprocess
git
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to ensure it only contains allowed characters
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {"status": "failed", "error": "Invalid host format"}
    try:
        output = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}