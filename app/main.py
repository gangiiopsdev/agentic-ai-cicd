from fastapi import FastAPI
import subprocess
def safe_subprocess_call(command: list) -> str:
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=10)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Failed with error: {e.stderr}"

class SafePingFastAPI(FastAPI):
    @app.get("/ping")
    def ping(self, host: str):
        if not self.is_safe_host(host):
            return {'status': 'error', 'message': 'Unsafe host'}
        command = ['ping', subprocess.check_output(f'echo {host}', shell=True).decode().strip()]
        output = safe_subprocess_call(command)
        return {'status': 'completed', 'output': output}

    def is_safe_host(self, host: str) -> bool:
        # Implement logic to check if the host is safe
        allowed_hosts = ['example.com', 'test.example.com']
        return host in allowed_hosts

app = SafePingFastAPI()