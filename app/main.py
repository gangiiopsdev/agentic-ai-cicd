from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safer implementation using subprocess.Popen with proper argument passing
        command = ['ping', self.host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
class PingEndpoint:
    def __init__(self):
        pass

    @staticmethod
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

    @staticmethod
def ping(host: str):
        if not host or ' ' in host:
            return {"error": "Invalid input"}
        ping_command = PingCommand(host)
        result = ping_command.execute()
        return {"status": "completed", "result": result}

app = FastAPI()

app.add_route("/ping", PingEndpoint.ping, methods=["GET"])