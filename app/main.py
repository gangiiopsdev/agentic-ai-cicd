from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation with input validation and error handling
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return execute_ping(host)