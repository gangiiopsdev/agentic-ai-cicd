from fastapi import FastAPI
import subprocess
class SanitizedProcess:
    def __init__(self, command):
        self.command = command.split()

    def run(self):
        try:
            result = subprocess.run(self.command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e.isspace())

@app.get("/ping")
def ping(host: str):    sanitized_host = sanitize_input(host)
    process = SanitizedProcess(['ping', sanitized_host])
    result = process.run()
    return {'status': 'completed', 'result': result}