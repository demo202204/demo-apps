"""Test Code"""
import pytest

from main import app


@pytest.fixture()
def client(request):
    app.config['TESTING'] = True
    test_client = app.test_client()
    yield test_client
    test_client.delete()


def vote(client, vote):
    return client.post('/', data=dict(vote=vote), follow_redirects=True)


def test_get(client):
    test_client = client
    result = test_client.get('/')
    """
    テスト処理実施
    """
    # assert テスト評価
    assert result.status_code == 200
    assert 'Azure Voting App' in result.get_data(as_text=True)


# def test_Fail(client):
#     # テスト失敗時
#     assert False
