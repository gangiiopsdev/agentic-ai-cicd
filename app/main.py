from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid host value')

    class SafeSubprocess:
        @staticmethod
        def run(command: str):
            args = shlex.split(command)
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode(), result.stderr.decode()

    class PingEndpoint:
        def __init__(self):
            self.app = FastAPI()

        @app.get("/ping")
        def ping_route(self, host: str):
            try:
                stdout, stderr = SafeSubprocess.run(f'ping {host}')
                return {"status": "completed", "stdout": stdout, "stderr": stderr}
            except subprocess.CalledProcessError as e:
                return {"status": "failed", "error": str(e)}

    if __name__ == "__main__":
        ping_endpoint = PingEndpoint()
        import uvicorn
        uvicorn.run(ping_endpoint.app, host="0.0.0.0", port=8000)