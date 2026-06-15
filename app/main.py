from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout

global_vars = globals()
def get_app():
    app = FastAPI()

    @app.get("/")
    def home():
        return {"message": "Agentic Self-Healing Pipeline"}

    @app.get("/ping")
    def ping(host: str):
        if not host.isalnum() or len(host) > 255:
            raise ValueError("Invalid host name")
        ping_command = PingCommand(host)
        status = ping_command.execute()
        return {"status": status}

    return app
global_vars['app'] = get_app()