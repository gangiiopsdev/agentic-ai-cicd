from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command_parts):
    return ' '.join(shlex.quote(part) for part in command_parts)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(safe_subprocess(['ping', host]).split(), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}