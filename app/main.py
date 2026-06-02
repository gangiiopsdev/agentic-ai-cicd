from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "error": str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)