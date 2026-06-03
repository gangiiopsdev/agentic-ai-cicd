from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        host = shlex.quote(host)
        args = ["ping", host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except Exception as e:
        return {"status": "failed", "error": str(e)}