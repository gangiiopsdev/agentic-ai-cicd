from fastapi import FastAPI
import subprocess
class SafeCommandRunner:
    @staticmethod
def run_command(command_parts):
        try:
            result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}

app = FastAPI()

def ping(host: str):
    safe_command_parts = ['ping', '-c', '1', host]
    return SafeCommandRunner.run_command(safe_command_parts)