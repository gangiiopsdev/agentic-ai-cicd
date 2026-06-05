from fastapi import FastAPI
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run()
        result = subprocess.run(['ping', '--'], capture_output=True, text=True, input=self.host)
        return result.stdout
global ping_command
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    ping_command_instance = PingCommand(host)
    return ping_command_instance.execute()