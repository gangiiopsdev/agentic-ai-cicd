from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command: str, args: list) -> None:
        if command in ['ping', 'traceroute'] and all(arg.isalnum() for arg in args):
            subprocess.run([command] + args, check=True)
        else:
            raise ValueError("Invalid or unsafe command")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        SafeSubprocess.run_command('ping', [host])
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}