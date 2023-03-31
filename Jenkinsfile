/*  This job running OpenCart web tests with pytest parameters:

- Number of threads (CMD_THREADS="1")
- Browser (CMD_BROWSER="chrome")
- Browser version (CMD_BROWSER_V="109")
- Executor (CMD_EXECUTOR="192.168.31.50")
- OpenCart url (CMD_OPENCART_URL=http://192.168.31.50:8081)
- Test filters (test: -k test_add_new_product_in_admin) (CMD_TEST_FILTERS="tests"/) */

pipeline {
    agent any
    environment {
        IMAGE_NAME="tests_image_jenkins"
        CONTAINER_NAME="tests_container_jenkins"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Innario/python-otus-web-module.git']]])
                sh 'ls -l'
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Innario/python-otus-web-module.git'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run --name ${CONTAINER_NAME} ${IMAGE_NAME} --url ${CMD_OPENCART_URL} --executor ${CMD_EXECUTOR} -n ${CMD_THREADS} --browser ${CMD_BROWSER} --bv ${CMD_BROWSER_V} ${CMD_TEST_FILTERS}'
                sh 'docker cp ${CONTAINER_NAME}:/app/allure-results .'
            }
            post{
                always{
                    allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
                }
            }
        }
        stage('Clean'){
            steps{
                sh """
                echo "Cleanup"
                docker stop $CONTAINER_NAME
                docker rm $CONTAINER_NAME
                docker rmi $IMAGE_NAME
                """
            }
        }
    }
}
