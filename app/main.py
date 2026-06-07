from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = self.sanitize_input(host)

    @staticmethod
def sanitize_input(input_string):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'  # Adjust as needed
        return ''.join(char for char in input_string if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    subprocess.call(['ping', command.host])
    return {"status": "completed"}