from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def safe_ping(self):
        # Safe implementation using subprocess.Popen
        command = ['ping', self.host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output, error

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_command = PingCommand(host)
    result, error = safe_command.safe_ping()
    if error:
        return {"error": error.decode()}
    else:
        return {"status": "completed", "output": result.decode()}