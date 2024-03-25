pipeline {
    agent any

    environment {
        IMAGE_NAME = 'tests'
        TAG = 'latest'
        INFRA_PATH = 'C:/Users/odehm/Desktop/repos/petsore/infra'
        LOGIC_PATH = 'C:/Users/odehm/Desktop/repos/petsore/logic'
        TEST_PATH = 'C:/Users/odehm/Desktop/repos/petsore/test'
        DOCKER_WORKDIR = '/usr/src/tests/petsore'
    }

    stages {
        stage('Debug') {
            steps {
                echo 'Starting parallel execution...'
            }
        }

        stage('Install pytest') {
            steps {
                bat 'call C:/Users/odehm/Desktop/repos/petsore/.venv/Scripts/pip.exe install pytest'
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                script {
                    parallel(
                        'Chrome Test': {
                            echo 'Running Chrome test...'
                            bat "python ${TEST_PATH}/End_to_End.py --browser chrome"
                        },
                        'Edge Test': {
                            echo 'Running Edge test...'
                            bat "python ${TEST_PATH}/End_to_End.py --browser edge"
                        },
                        'Firefox Test': {
                            echo 'Running Firefox test...'
                            bat "python ${TEST_PATH}/End_to_End.py --browser firefox"
                        }
                    )
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Uncomment the line below if you want to remove the Docker image
            // bat "docker rmi ${IMAGE_NAME}:${TAG}"
        }
        success {
            echo 'Generating HTML report...'
            bat "call C:/Users/odehm/Desktop/repos/petsore/.venv/Scripts/pytest --html=${TEST_PATH}/report.html ${TEST_PATH}"
            publishHTML(target: [reportDir: '${TEST_PATH}', reportFiles: 'report.html', reportName: 'Test Report'])
        }
    }
}
