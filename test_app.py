@pytest.fixture(scope='session', autouse=True)
def setup_database():

    init_db()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.get_json() == {"status": "ok"}
def test_resources(client):
    rv = client.get('/api/resources/helplines')
    assert rv.status_code == 200
    data = rv.get_json()
    assert 'pakistan' in data


def test_crisis_keyword(client):
    post_data = {
        "alias": "Test User",
        "content": "I want to end it all, please help."
    }
    rv = client.post('/api/posts', json=post_data)
    assert rv.status_code == 201
    data = rv.get_json()
    assert data['status'] == "Success"

def test_empty_post_error(client):
    rv = client.post('/api/posts', json={})
    assert rv.status_code == 400