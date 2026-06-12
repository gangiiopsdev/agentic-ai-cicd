from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_executable_path(executable):
    return executable in [os.path.basename(path) for path in os.environ['PATH'].split(os.pathsep)]

@app.get("/ping")
def ping(host: str):
    try:
        if not safe_executable_path("ping") or host.startswith(('-', '--')):
            raise ValueError("Invalid command arguments")
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}