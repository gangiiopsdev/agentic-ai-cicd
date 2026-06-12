from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen
    if host.isnumeric() or '@' in host:
        return {"status": "invalid", "output": None, "error": "Invalid host input."}
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode()}