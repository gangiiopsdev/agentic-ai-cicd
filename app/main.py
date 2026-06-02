from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        completed_process = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            *args,
            **kwargs
        )
        return completed_process.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = SafeSubprocess.run(["ping", host], capture_output=False)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}