from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Using check_output instead of call for better error handling and security
            result = subprocess.check_output(['ping', subprocess.list2cmdline([self.host])], stderr=subprocess.STDOUT)
            return result.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"Ping failed: {e.output.decode('utf-8')}""]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()