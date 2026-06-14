from fastapi import FastAPI
import subprocess

async def safe_ping(host: str):
    # Safe implementation using list arguments for subprocess.call
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class PingEndpoint:
    app = FastAPI()

    @app.get("/ping")
    async def ping(host: str):
        if not is_safe_host(host):
            return {"error": "Invalid host"}
        try:
            response = await safe_ping(host)
            return {"status": "completed", "response": response}
        except Exception as e:
            return {"error": str(e)}

    def is_safe_host(host: str):
        # Implement your logic to check if the host is safe
        allowed_hosts = ['127.0.0.1', '::1']
        return host in allowed_hosts