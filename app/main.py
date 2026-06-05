from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        command = ['ping', *shlex.split(host)]
        output = subprocess.run(command, capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}