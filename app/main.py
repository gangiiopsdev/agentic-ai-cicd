from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_commands = ['ping']

    async def execute_ping(self, host):
        if host not in self.safe_commands:
            return 'Host not allowed'
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True)
            return output.stdout
        except Exception as e:
            return str(e)

global_safe_ping = SafePing()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = global_safe_ping.execute_ping(host)
    return {"status": "completed", "result": result}