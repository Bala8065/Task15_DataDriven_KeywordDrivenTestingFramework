import pytest
from pages.login_page import LoginPage
from utils.excel_utils import read_test_data, write_result

# Read Excel test data
test_data = read_test_data()


@pytest.mark.parametrize("data", test_data)
def test_login(driver, data):
    """
    Test login functionality using data-driven approach
    """
    login_page = LoginPage(driver)  # ✅ Create instance

    # Perform login
    login_page.login(data["username"], data["password"])

    # Expected outcome (only Admin/admin123 should succeed)
    expected = True if data["username"] == "Admin" and data["password"] == "admin123" else False

    # Actual outcome
    actual = login_page.is_login_successful()  # ✅ Now calls instance method

    # Write result to Excel
    if actual == expected:
        write_result(data["test_id"], "Passed")
        assert True
    else:
        write_result(data["test_id"], "Failed")
        assert False
