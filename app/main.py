from fastapi import FastAPI
import subprocess
def run_safe_command(command_parts):
    result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
    return result.stdout
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            safe_command = ['ping', host]
            output = run_safe_command(safe_command)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}
app = FastAPI()
app.add_api_route('/ping', SafePing.ping, methods=['GET'])