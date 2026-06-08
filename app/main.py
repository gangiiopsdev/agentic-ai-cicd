from fastapi import FastAPI
import subprocess
cimport shlex
cdef safe_subprocess_call(command: str):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

cdef ping(host: str):
    command = f"ping {host}"
    return safe_subprocess_call(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_subprocess_call(f"ping {host}")
    return {"status": "completed", "result": result}