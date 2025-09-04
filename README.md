# Task15 OrangeHRM Data-Driven Testing Framework

## 📌 Project Overview

This project demonstrates a **data-driven test automation framework** using:

* **Python + Pytest** for test execution and reporting
* **Selenium** for browser automation
* **Page Object Model (POM)** for maintainable test design
* **OpenPyXL** for Excel-based test data management
* **Explicit Wait + Expected Conditions** (no `sleep()` used)

It automates the login functionality of the OrangeHRM demo portal:
🔗 [https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)

---

## 📂 Project Structure

```
Task15_DataDriven_KeywordDrivenTestingFramework/
│
├── tests/
│   ├── test_login.py        # Main test cases
│   └── conftest.py          # WebDriver fixture
│
├── pages/
│   └── login_page.py        # Page Object Model for login
│
├── utils/
│   └── excel_utils.py       # Excel read/write helper functions
│
├── data/
│   └── login_data.xlsx      # Test data (username, password, etc.)
│
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

---

## ⚙️ Setup Instructions

1. **Clone or Download the Project**

   ```bash
   git clone <repo-url>
   cd Task15_DataDriven_KeywordDrivenTestingFramework
   ```

2. **Create Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure ChromeDriver is Installed**

   * Download ChromeDriver matching your Chrome version:
     [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
   * Add it to your system PATH.

---

## ▶️ Running Tests

### Run all tests

```bash
pytest --html=report.html --self-contained-html
```

### Run specific test

```bash
pytest tests/test_login.py::test_login
```

---

## 📝 Test Data

The Excel file `data/login_data.xlsx` contains the test cases:

| TestID | Username  | Password  | Date | Time | Tester | Result |
| ------ | --------- | --------- | ---- | ---- | ------ | ------ |
| 1      | Admin     | admin123  |      |      | Kumar  |        |
| 2      | WrongUser | wrongPass |      |      | Kumar  |        |
| 3      | Admin     | wrongPass |      |      | Kumar  |        |
| 4      | WrongUser | admin123  |      |      | Kumar  |        |
| 5      | Admin     | admin123  |      |      | Kumar  |        |

* **Valid credentials** → login should succeed
* **Invalid credentials** → login should fail

Test results, along with **date & time**, will be written back into this Excel file after each test run.

---

## 📊 Reports

Pytest generates an HTML report after test execution:

```bash
pytest --html=report.html --self-contained-html
```

Open `report.html` in your browser to view the summary.

---

## 🙌 Author

* **Kumar**
* Automated Testing using **Pytest + Selenium + Excel + POM**

---

