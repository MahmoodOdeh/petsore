pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
        INFRA_PATH = 'C:/Users/odehm/Desktop/new/AirbnbSeleniumGridProject/infra'
        LOGIC_PATH = 'C:/Users/odehm/Desktop/new/AirbnbSeleniumGridProject/logic'
    }

    stages {
        stage('Debug') {
            steps {
                echo 'Starting parallel execution...'
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                script {
                    parallel(
                        'Chrome Test': {
                            echo 'Running Chrome test...'
                            bat "docker rm -f chrome_test || true"
                            bat "docker run --name chrome_test -e PYTHONPATH=/usr/src/tests/AirbnbSeleniumGridProject -v ${INFRA_PATH}:/usr/src/tests/AirbnbSeleniumGridProject/infra -v ${LOGIC_PATH}:/usr/src/tests/AirbnbSeleniumGridProject/logic ${IMAGE_NAME}:${TAG} python test/world_page_test.py --browser chrome"
                        },
                        'Edge Test': {
                            echo 'Running Edge test...'
                            bat "docker rm -f edge_test || true"
                            bat "docker run --name edge_test -e PYTHONPATH=/usr/src/tests/AirbnbSeleniumGridProject -v ${INFRA_PATH}:/usr/src/tests/AirbnbSeleniumGridProject/infra -v ${LOGIC_PATH}:/usr/src/tests/AirbnbSeleniumGridProject/logic ${IMAGE_NAME}:${TAG} python test/world_page_test.py --browser edge"
                        },
                        'Firefox Test': {
                            echo 'Running Firefox test...'
                            bat "docker rm -f firefox_test || true"
                            bat "docker run --name firefox_test -e PYTHONPATH=/usr/src/tests/AirbnbSeleniumGridProject -v ${INFRA_PATH}:/usr/src/tests/AirbnbSeleniumGridProject/infra -v ${LOGIC_PATH}:/usr/src/tests/AirbnbSeleniumGridProject/logic ${IMAGE_NAME}:${TAG} python test/world_page_test.py --browser firefox"
                        }
                    )
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // bat "docker rmi ${IMAGE_NAME}:${TAG}"
        }
    }
}
