from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = ''.join(filter(str.isalnum, host))
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)