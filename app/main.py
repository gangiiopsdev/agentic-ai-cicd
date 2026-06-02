from fastapi import FastAPI
import subprocess
import shlex

global_params = {
    'ping': ['ping', '-c', '4']
}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    if host in global_params:
        command = global_params[host]
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            return {"output": result.stdout, "error": result.stderr}
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Invalid host"}