def test_unregister_removes_participant(client):
    activity_name = "Chess Club"
    email = "daniel@mergington.edu"

    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    updated = client.get("/activities").json()
    assert email not in updated[activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown%20Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_non_registered_student(client):
    response = client.delete(
        "/activities/Chess%20Club/signup",
        params={"email": "not.registered@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not registered for this activity"
