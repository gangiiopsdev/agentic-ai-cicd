from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split('ping ' + host)
        output = subprocess.run(args, shell=False, capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}