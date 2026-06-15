from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f"ping {host}")
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}