from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host parameter"}
    command = PingCommand(host)
    result = command.execute()
    return {"status": "completed", "result": result}

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for IP address format
    return True