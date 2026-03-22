import urllib.request
import urllib.error
import json

def test_login(data, desc):
    print(f"\n--- Probando: {desc} ---")
    req = urllib.request.Request(
        'http://localhost:8000/login/',
        data=data.encode('utf-8') if data else None,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        response = urllib.request.urlopen(req)
        print(f"Status: {response.status}")
        print(f"Body: {response.read().decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"Status: {e.code}")
        print(f"Body: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")

test_login('invalid json {', 'JSON Malformado')
test_login(json.dumps({'username': 'admin'}), 'Falta Password')
test_login(json.dumps({'username': 'fake_user', 'password': '123'}), 'Usuario Falso')
