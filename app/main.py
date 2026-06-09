from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.replace('.', '', 3).isdigit():
            raise ValueError("Invalid IP address")
        result = subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr.decode())}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}