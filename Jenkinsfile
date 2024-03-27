pipeline {
    agent any
    environment {
        PYTHON_EXECUTABLE='C:/Users/odehm/Desktop/seleniumGrid/PetStore/.venv/Scripts/python.exe'
        PYTHONPATH = "C:/Users/odehm/Desktop/repos/petsore"
        TEST_REPORTS='test-reports'
        PIP_EXECUTABLE='C:/Users/odehm/Desktop/seleniumGrid/PetStore/.venv/Scripts/pip.exe'
        PYTEST_EXECUTABLE='C:/Users/odehm/Desktop/seleniumGrid/PetStore/.venv/Scripts/pytest.exe'
        PASSWORD = credentials('JIRA_TOKEN')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                bat "${PIP_EXECUTABLE} install -r requirements.txt" // Install dependencies if needed
            }
        }
        stage('Test UI') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat "${PYTHON_EXECUTABLE} test/test_ui/login_test.py -k test_run_grid_parallel_test_wrong_data_login"
            }
        }
        stage('Run Tests UI') {
            steps {
                echo 'Running Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "${PYTEST_EXECUTABLE} test/test_ui/login_test.py -k test_run_grid_parallel_test_wrong_data_login --html=test-reports/report.html"
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage('Test PII') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat "${PYTHON_EXECUTABLE} test/test_api/test_cart.py -k test_run_grid_parallel_test_add_product"
            }
        }
        stage('Run Tests API') {
            steps {
                echo 'Running Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "${PYTEST_EXECUTABLE} test/test_api/test_cart.py -k test_run_grid_parallel_test_add_product --html=test-reports/report.html"
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage('Test NON_FUNCTIONAL') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat "${PYTHON_EXECUTABLE} test/non_functional/performance_test.py -k test_run_grid_parallel_test_assert_response_time_search"
            }
        }
        stage('Run Tests NON_FUNCTIONAL') {
            steps {
                echo 'Running Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "${PYTEST_EXECUTABLE} test/non_functional/performance_test.py -k test_run_grid_parallel_test_assert_response_time_search --html=test-reports/report.html"
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
          stage('Test END_TO_END') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat "${PYTHON_EXECUTABLE} test/End_to_End.py -k test_run_grid_parallel_test_get_quantity"
            }
        }
        stage('Run Tests END_TO_END') {
            steps {
                echo 'Running Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "${PYTEST_EXECUTABLE} test/End_to_End.py -k test_run_grid_parallel_test_get_quantity --html=test-reports/report.html"
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Add deployment steps here if needed
            }
        }
    }
}
