from fastapi.testclient import TestClient
from app.main import app

c = TestClient(app, raise_server_exceptions=False)
print('POST new  :', c.post('/students', json={'name': 'Ravi', 'email': 'ravi@test.com'}).status_code)
print('GET  1    :', c.get('/students/1').status_code)
r = c.post('/students', json={'name': 'Ravi', 'email': 'ravi@test.com'})
print('POST dup  :', r.status_code, r.json())
r = c.get('/students/99')
print('GET  99   :', r.status_code, r.json())
