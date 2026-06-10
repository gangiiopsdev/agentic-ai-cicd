from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isalnum():
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid input"}