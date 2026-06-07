from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    command = PingCommand(host)
    result = command.execute()
    return {'status': 'completed', 'stdout': result.stdout}

def valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., using regex to check for allowed characters and format
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return pattern.match(host) is not None