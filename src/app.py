import json
from pathlib import Path

import yaml
from environs import Env
from fastapi import FastAPI
from zenroom.zenroom import zencode_exec

app = FastAPI()
env = Env()
env.read_env()

conf_file = env("RESTROOM_CONFIG_FILE")
conf = yaml.load(Path(conf_file).read_text(), Loader=yaml.BaseLoader)


def __load_file(zenfile):
    return Path(f"{conf['zen_folder']}/{zenfile}")


def make_function(filename):
    def _function(data: str = None, keys: str = None):
        script = Path(filename).read_text()
        result = zencode_exec(script=script, keys=keys, data=data)
        return {"err": result.stderr, "out": json.loads(result.stdout) }
    return _function


for _ in conf["get"]:
    filename = __load_file(_)
    app.add_api_route(f'/{filename.stem}', make_function(filename), methods=['get'])

for _ in conf["post"]:
    filename = __load_file(_)
    app.add_api_route(f'/{filename.stem}', make_function(filename), methods=['post'])