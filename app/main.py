from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        # Secure implementation using shlex.quote to escape special characters in the hostname
        command = ['ping', shlex.quote(self.host)]
        subprocess.call(command)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    await ping_command.run()
    return {"status": "completed"}