from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum():  # Example validation, adjust as needed
        return {"status": "error", "message": "Invalid input"}
    args = shlex.split('ping ' + host)
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    return {"status": "completed", "output": result.stdout.decode()}