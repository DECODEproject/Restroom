import json
from pathlib import Path
from environs import Env
from fastapi import FastAPI
from zenroom.zenroom import zencode_exec

app = FastAPI(title="RESTRoom")
env = Env()
env.read_env()

conf_file = env("RESTROOM_CONFIG_FILE")
conf = Path(conf_file).read_text().split('\n')


def make_function(script):
    def _function(data: str = None, keys: str = None):
        result = zencode_exec(script=script, keys=keys, data=data)
        return {"err": result.stderr, "out": json.loads(result.stdout) }
    return _function


for _ in conf:
    method, route, filename = _.split(" ")
    script = Path(filename).read_text()
    app.add_api_route(route,
                      make_function(script),
                      methods=[method],
                      description=script,
                      summary=script,
                      tags=['Zencode'])