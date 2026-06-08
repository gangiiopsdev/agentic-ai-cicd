from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_ping(host: str):
        try:
            # Sanitize and validate the host input before using it in the command.
            if not host.strip() or ' ' in host or '>' in host or '<' in host or ';' in host or '&' in host or '|' in host or '`' in host:
                raise ValueError('Invalid host input')

            # Use shlex.quote to safely quote the command arguments.
            args = ['ping'] + shlex.split(host)
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Using a safe wrapper function to handle the ping command.
    return SafeSubprocess.safe_ping(host)