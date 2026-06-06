from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    response_model=str,
    responses={200: {'description': 'Operation completed successfully'}},
)
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()