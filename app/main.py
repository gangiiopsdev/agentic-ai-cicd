from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def sanitize_input(user_input):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return ''.join(filter(lambda x: x in allowed_chars, user_input))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = PingCommand.sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}