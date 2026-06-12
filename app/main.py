from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.commands = {"ping": True}

    def execute(self, cmd: str, args: list = None) -> bool:
        if args and len(args) > 0 and args[0] in self.commands:
            sanitized_args = [arg.replace(';', '').replace('&', '').replace('|', '') for arg in args]
            return subprocess.call([cmd, *sanitized_args], shell=False) == 0
        return False
class PingEndpoint:
    def __init__(self):
        self.safe_ping = SafePing()

    @app.get("/ping")
    def ping(self, host: str):
        if self.safe_ping.execute("ping", [host]):
            return {"status": "completed"}
        else:
            return {"status": "failed"}