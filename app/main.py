from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command: str):
        self.command = command

    def execute(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.command], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
global_vars = globals()
local_vars = locals()
globals_dict = dir(globals())
locals_dict = dir(locals())
for var_name in globals_dict + locals_dict:
    if var_name.startswith('__') and var_name.endswith('__'):
        del globals()[var_name]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 64:
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        ping_command = PingCommand(host)
        result = ping_command.execute()
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}