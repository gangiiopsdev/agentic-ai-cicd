from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> None:
        args = ['ping', self.host]
        subprocess.run(args, check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str): 
    if not re.match(r'^\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b$', host):
        raise HTTPException(status_code=400, detail="Invalid IP address")
    ping_command = PingCommand(host)
    ping_command.execute()