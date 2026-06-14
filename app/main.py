from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if ';' in host or '&&' in host:
        raise Exception('Invalid input')
    args = ["ping", host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'stdout': result.stdout}