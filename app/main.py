from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host parameter
        if not all(c.isalnum() or c in '.-' for c in host):
            raise ValueError("Invalid host parameter")
        # Using a safe method to execute the command
        subprocess.run(['ping', shlex.quote(host)], shell=False, check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}