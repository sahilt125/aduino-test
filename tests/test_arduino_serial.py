

def test_ping(board):
    response = board.query("t")
    assert response == "Arduino is alive!"


def test_blink_100(board):
    response = board.query("1")
    assert response == "OK: 100"


def test_blink_500(board):
    response = board.query("2")
    assert response == "OK: 500"


def test_status(board):
    board.query("2")
    response = board.query("s")
    assert "500" in response