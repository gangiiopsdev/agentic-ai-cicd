from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    response = PingCommand.execute(host)
    return {"status": "completed", "output": response}