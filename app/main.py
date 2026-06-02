from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    if not host.isnumeric():
        return {"error": "Invalid input"}
    command = ['ping', host]
    try:
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)