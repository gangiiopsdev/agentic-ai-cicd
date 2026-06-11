from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: list) -> None:
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(e.stderr)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"error": "Invalid input"}
    command = shlex.split(f'ping {host}')
    SafeSubprocess.call(command)
    return {"status": "completed"}