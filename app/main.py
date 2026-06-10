from fastapi import FastAPI
import subprocess
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
    SafeSubprocess.call(["ping", host])
    return {"status": "completed"}