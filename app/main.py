from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            result = subprocess.run(['ping', '-c', '4', self.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand(host)
    output = command_executor.run()
    return {"status": "completed", "output": output}