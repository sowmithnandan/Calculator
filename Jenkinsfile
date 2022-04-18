pipeline {
    environment {
        imagename = "sowmithnandan1/calculator"
        registryCredential = "sowmithnandanDockerHub"
        dockerImage = ''
        }

    
    agent none

    stages {
        stage('Pull') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile calculator.py '
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml calcTest.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Build')
        {
            agent any 
            steps 
                {
                script
                    {
                    dockerImage = docker.build imagename
                    }
                }
        }
        stage('Docker Image push')
        {
            agent any
            steps
               {
                script
                    {
                    docker.withRegistry( '', registryCredential ){
                    dockerImage.push()
                    } 
                }
                }
        }
        stage('Ansible')
        {
            agent any
            steps 
                {
                sh 'pwd'
                sh 'ls'
                ansiblePlaybook colorized: true, disableHostKeyChecking: true, installation: "Ansible", inventory: 'Inv.inv',playbook:'Playbook.yml'
                }
        }
    }
}