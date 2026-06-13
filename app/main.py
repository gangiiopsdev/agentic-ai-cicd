from fastapi import FastAPI
import subprocess
class Pinger:
    def __init__(self):
        self.allowed_hosts = {'localhost', '127.0.0.1'}

    async def ping(self, host: str) -> dict:
        if host.strip() not in self.allowed_hosts:
            return {'status': 'unauthorized'}
        try:
            # Validate and sanitize the input
            subprocess_args = ['ping', '-c', '4', subprocess.check_output(f'echo {host}', shell=True, text=True).strip()]
            result = await subprocess.run(subprocess_args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except (subprocess.CalledProcessError, subprocess.SubprocessError) as e:
            return {'status': 'failed', 'error': str(e)}