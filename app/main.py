from fastapi import FastAPI
import subprocess
class CommandExecutor:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts

    def execute_command(self, command, host=None):
        if host and host not in self.allowed_hosts:
            raise ValueError('Host is not allowed')
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()
executor = CommandExecutor(allowed_hosts=['127.0.0.1', '::1'])

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    try:
        output = executor.execute_command(command, host)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"error": str(e)}