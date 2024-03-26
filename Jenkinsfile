pipeline {
    agent any
    environment {
        PYTHON_EXECUTABLE='C:/Users/odehm/Desktop/seleniumGrid/PetStore/.venv/Scripts/python.exe'
        PYTHONPATH = "C:/Users/odehm/Desktop/repos/petsore"
        TEST_REPORTS='test-reports'
        PIP_EXECUTABLE='C:/Users/odehm/Desktop/seleniumGrid/PetStore/.venv/Scripts/pip.exe'
        PYTEST_EXECUTABLE='C:/Users/odehm/Desktop/seleniumGrid/PetStore/.venv/Scripts/pytest.exe'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                bat "${PIP_EXECUTABLE} install -r requirements.txt" // Install dependencies if needed
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat "${PYTHON_EXECUTABLE} test/End_to_End.py"
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "${PYTEST_EXECUTABLE} test/End_to_End.py --html=test-reports/report.html"
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
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