from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.safe_commands = {'ping': ['ping', '-c', '4']}  # Example safe commands with parameters

    def is_safe_command(self, command: str) -> bool:
        return command in self.safe_commands.keys()

    def execute(self, command: str, host: str):
        if not self.is_safe_command(command):
            raise ValueError('Invalid command')
        args = shlex.split(f'{self.safe_commands[command]} {host}')
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.stderr.decode()}'

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping_instance.execute('ping', host)}