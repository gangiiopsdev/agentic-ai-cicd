from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host.isalpha() and len(host) <= 32:
        try:
            # Use shlex.split to ensure safe splitting of the command
            args = ['ping'] + shlex.split(host)
            subprocess.run(args, check=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"error": f"Failed to ping host: {e}"}
    else:
        return {"error": "Invalid input"}