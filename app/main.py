from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str):
        try:
            subprocess.run(shlex.split(command), check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Command failed with return code {e.returncode}: {str(e)}")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        SafeSubprocess.run(shlex.quote('ping') + ' ' + shlex.quote(host))
    except Exception as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}