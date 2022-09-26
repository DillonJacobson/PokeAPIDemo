import pytest

from app import app

def test_pokedex():
    response = app.test_client().get('/api/pokedex')
    assert response.status_code == 200
    data = response.get_json()
    assert 'pokemon' in data
    assert len(data['pokemon']) == 5