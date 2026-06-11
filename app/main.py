from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        pass

    def ping(self, host: str):
        try:
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return output.stdout.strip()
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand()
    result = ping_command.ping(host)
    return {"status": "completed", "result": result}