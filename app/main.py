from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not self.is_valid_host(host):
        raise ValueError("Invalid host")
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {"status": "completed", "result": result}

@staticmethod
def is_valid_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe
def validate_input(input_value: str) -> bool:
    # Custom function to validate input against known risks