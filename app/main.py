from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command_parts):
        try:
            subprocess.run(command_parts, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Command failed with error: {e}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_parts = ["ping", shlex.quote(host)]
    SafeSubprocess.run(command_parts)
    return {"status": "completed"}