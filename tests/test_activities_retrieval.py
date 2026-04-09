def test_get_activities_returns_expected_structure(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

    chess = data["Chess Club"]
    assert set(chess.keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(chess["description"], str)
    assert isinstance(chess["schedule"], str)
    assert isinstance(chess["max_participants"], int)
    assert isinstance(chess["participants"], list)
