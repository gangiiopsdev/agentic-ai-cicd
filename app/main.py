from fastapi import FastAPI
import subprocess
import shlex


global_app = FastAPI()

def ping(host: str):
    # Validate and escape input to prevent shell injection
    host = shlex.quote(host)
    try:
        subprocess.run(["ping", host], check=True, text=True, capture_output=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}


global_app.add_api_route("/ping", ping, methods=["GET"])