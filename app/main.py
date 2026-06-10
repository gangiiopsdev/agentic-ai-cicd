from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await self._execute_ping()

    async def _execute_ping(self):
        command = ["ping", self.host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand(None)

    async def ping_host(self, host: str):
        self.ping_command.host = host
        result = await self.ping_command.execute()
        return {"status": "completed", "result": result}

class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()
        self.ping_endpoint = PingEndpoint()

    def add_routes(self):
        @self.app.get("/ping")
        async def ping(host: str):
            return await self.ping_endpoint.ping_host(host)
class AppRunner:
    def __init__(self):
        self.fast_api_app = FastAPIApp()

    def run(self):
        app = self.fast_api_app.app
        self.fast_api_app.add_routes()
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
class Application:
    @staticmethod
def main():
        runner = AppRunner()
        runner.run()if __name__ == "__main__":
    Application.main()