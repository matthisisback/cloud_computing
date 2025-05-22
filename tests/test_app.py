import pytest
from src.app import app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_events_endpoint(client):
    response = client.get('/api/events')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_news_endpoint(client):
    response = client.get('/api/news')
    assert response.status_code == 200
    assert isinstance(response.json, list)
