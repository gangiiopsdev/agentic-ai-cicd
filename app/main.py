from fastapi import FastAPI
import subprocess
def run_safe_command(command_parts):
    result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
    return result.stdout
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = host.replace(';', '').replace('&', '')  # Basic input sanitization
        safe_command = ['ping', safe_host]
        output = run_safe_command(safe_command)
        return {'status': 'completed', 'output': output}
app = FastAPI()
app.add_api_route('/ping', SafePing.ping, methods=['GET'])