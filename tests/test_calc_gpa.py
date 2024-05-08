from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_calc_gpa_single():
    response = client.get("/calc_gpa/1")
    assert response.text == "1.00"

    response = client.get("/calc_gpa/5.5")
    assert response.text == "5.50"


def placeholder_test_calc_gpa_multiple():
    pass


def placeholder_test_calc_gpa_more_values():
    pass


def placeholder_test_calc_gpa_rounding():
    pass


def placeholder_test_calc_gpa_positive_numbers_only():
    pass


def placeholder_test_calc_gpa_handle_spaces():
    pass
