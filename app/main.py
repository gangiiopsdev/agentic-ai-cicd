from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
global_host = 'example.com'  # Define a global safe default value for host

app = FastAPI()

@app.get("/ping")
def ping(host: str = global_host):  # Use the global safe default value for host
    result = PingCommand(host).execute()
    return {"status": "completed", "result": result}