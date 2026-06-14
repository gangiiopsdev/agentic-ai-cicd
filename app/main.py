from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

safe_commands = {
    'ping': ['ping', '-c', '1']
}
cmd_app = FastAPI()

cmd_app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

cmd_app.get("/ping")
def ping(host: str):
    if host in safe_commands['ping']:
        result = execute_command(safe_commands['ping'] + [host])
        return {"status": "completed", "result": result}
    else:
        return {"status": "error", "message": "Invalid command"}