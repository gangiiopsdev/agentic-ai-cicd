from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def sanitize_input(user_input):
        safe_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return ''.join(char for char in user_input if char in safe_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = PingCommand.sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)
    return {"status": "completed"}