import tomllib

from fastapi import FastAPI


def get_app_version() -> str | None:
    version = None
    with open('./pyproject.toml') as f:
        f_str = f.read()
        pyproject = tomllib.loads(f_str)
        project = pyproject.get('project', {}) or {}
        version = project.get('version')
    return version


app = FastAPI(
    title='simple-fastapi-app',
    version=get_app_version(),
)


@app.get(path='/health')
async def get_health() -> dict:
    return {'status': 'ok'}


@app.get(path='/info')
async def get_info() -> dict:
    return {'version': get_app_version()}
