pipeline {
    agent any

    environment {
        // Define the Docker image name
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
                script {
                    echo 'Installing pytest...'
                    bat 'C:\\Users\\odehm\\Desktop\\seleniumGrid\\final\\env\\Scripts\\pip.exe install pytest'
                     bat   bat 'call venv\\Scripts\\python.exe -m pytest /test/End_to_End.py  --html=${TEST_REPORTS}\\report.html --self-contained-html'
                }
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                script {
                    parallel(
                        'Chrome Test': {
                            echo 'Running Chrome test...'
                            bat "docker rm -f chrome_test || true"
                            bat "docker run --name chrome_test -e PYTHONPATH=${DOCKER_WORKDIR} -v ${INFRA_PATH}:${DOCKER_WORKDIR}/infra -v ${LOGIC_PATH}:${DOCKER_WORKDIR}/logic -v ${TEST_PATH}:${DOCKER_WORKDIR}/test ${IMAGE_NAME}:${TAG} python ${DOCKER_WORKDIR}/test/End_to_End.py --browser chrome"
                        },
                        'Edge Test': {
                            echo 'Running Edge test...'
                            bat "docker rm -f edge_test || true"
                            bat "docker run --name edge_test -e PYTHONPATH=${DOCKER_WORKDIR} -v ${INFRA_PATH}:${DOCKER_WORKDIR}/infra -v ${LOGIC_PATH}:${DOCKER_WORKDIR}/logic -v ${TEST_PATH}:${DOCKER_WORKDIR}/test ${IMAGE_NAME}:${TAG} python ${DOCKER_WORKDIR}/test/End_to_End.py --browser edge"
                        },
                        'Firefox Test': {
                            echo 'Running Firefox test...'
                            bat "docker rm -f firefox_test || true"
                            bat "docker run --name firefox_test -e PYTHONPATH=${DOCKER_WORKDIR} -v ${INFRA_PATH}:${DOCKER_WORKDIR}/infra -v ${LOGIC_PATH}:${DOCKER_WORKDIR}/logic -v ${TEST_PATH}:${DOCKER_WORKDIR}/test ${IMAGE_NAME}:${TAG} python ${DOCKER_WORKDIR}/test/End_to_End.py --browser firefox"
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
        success {
            echo 'Generating HTML report...'
            bat "docker run --rm -v ${TEST_PATH}:${DOCKER_WORKDIR}/test -w ${DOCKER_WORKDIR}/test ${IMAGE_NAME}:${TAG} pytest --html=report.html"
            publishHTML(target: [reportDir: '${DOCKER_WORKDIR}/test', reportFiles: 'report.html', reportName: 'Test Report'])
        }
    }
}
