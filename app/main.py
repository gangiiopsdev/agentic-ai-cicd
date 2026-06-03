from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', '-c', '1', '--'] + [host]  # Using '--' to separate options from arguments
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get="/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}