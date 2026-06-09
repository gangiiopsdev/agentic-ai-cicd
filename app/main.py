from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if not all(char.isalnum() for char in host):
            raise ValueError("Invalid input")
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}