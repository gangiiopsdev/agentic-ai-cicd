from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host: str) -> bool:
    # More robust validation logic here
    return host.isnumeric() or '@' in host or '.' in host

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "invalid", "output": None, "error": "Invalid host input."}
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode()}