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

@cmd_app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

cmd_app.get("/ping")
def ping(host: str):
    if host in safe_commands['ping']:
        result = execute_command(safe_commands['ping'] + [host])
        return {"status": "completed", "result": result}
    else:
        return {"status": "error", "message": "Invalid command"}
def secure_execute_command(command):
    if isinstance(command, list) and len(command) > 0:
        for arg in command:
            if not isinstance(arg, str):
                raise ValueError("Command arguments must be strings")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    else:
        raise ValueError("Invalid command format")
cmd_app.get("/secure_ping")
def secure_ping(host: str):
    if host in safe_commands['ping']:
        try:
            result = secure_execute_command(safe_commands['ping'] + [host])
            return {"status": "completed", "result": result}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    else:
        return {"status": "error", "message": "Invalid command"}