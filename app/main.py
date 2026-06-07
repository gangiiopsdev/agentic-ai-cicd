from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid host value')

    class PingEndpoint:
        def __init__(self):
            self.app = FastAPI()

        @app.get("/ping")
        async def ping_route(self, host: str):
            try:
                result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
            except subprocess.CalledProcessError as e:
                return {"status": "failed", "error": str(e)}

    if __name__ == "__main__":
        ping_endpoint = PingEndpoint()
        import uvicorn
        uvicorn.run(ping_endpoint.app, host="127.0.0.1", port=8000)