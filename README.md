# petsore
Setup
Clone the repository:

sh
Copy code
git clone https://github.com/MahmoodOdeh/petsore.git
cd petstore-automation
Install dependencies:

sh
Copy code
pip install -r requirements.txt
Configure Selenium Grid:

Set up your Selenium Grid hub and nodes. Ensure that your hub and nodes are running and accessible.
Configure Jenkins:

Set up a Jenkins job for this project, pointing to your Git repository.
Configure the Jenkins job to run the tests using the command: pytest --html=reports/report.html.
Configure Jira integration:

Generate a Jira API token for authentication.
Update the config.py file with your Jira username, password (API token), and Jira project details.
Running Tests
To run the tests locally, use the command:

sh
Copy code
pytest --html=reports/report.html
To run the tests on Selenium Grid, ensure that the Selenium Grid hub and nodes are running, and use the command:

sh
Copy code
pytest --html=reports/report.html --remote=http://your-grid-hub:4444/wd/hub
Project Structure
infra/: Contains infrastructure-related code, such as setting up the Selenium WebDriver.
logic/: Contains logic for interacting with the website, following the Page Object Model (POM).
test/: Contains test cases that use the logic and infrastructure layers to perform QA tests.
Reports
HTML reports for test results are generated in the reports/ directory after each test run.
Jira Integration
Bugs discovered during test execution are reported directly to Jira, linking back to the failing test case.
Contributing
Feel free to contribute by opening issues or submitting pull requests.
 
