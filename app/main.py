from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if any(char in host for char in [";", "&&"]):
        raise Exception("Invalid input")
    args = shlex.split(f"ping {host}")
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'stdout': result.stdout}