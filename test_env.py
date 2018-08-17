import json
import run

def test_app():
    assert run.app

def test_zappa_settings():
    with open('zappa_settings.json') as file:    
        data = json.load(file)
        assert data['dev']['app_function'] == "run.app"
