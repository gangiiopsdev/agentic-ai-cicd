from fastapi import FastAPI
import subprocess
class CommandRunner:
    def run(self, command: list):
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

# Ensure the input is sanitized or validated before execution
@fastapi.Depends(validate_input)
def ping(host: str):
    args = ['ping', host]
    output = cmd_runner.run(args)
    return {'status': 'completed', 'output': output}

def validate_input(host: str) -> str:
    # Implement validation logic here
    if not is_valid_host(host):
        raise ValueError('Invalid input')
    return host