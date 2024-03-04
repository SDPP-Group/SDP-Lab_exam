pipeline {
    agent any
    stages{
        stage('Run unit-test'){
            agent{
                label 'testNode'
            }
            steps{
                echo 'Run unit-test'
                sh 'python3 exam-unittest.py'
                echo 'Done'
            }
        }
        stage('Create images of api'){
            agent{
                label 'testNode'
            }
            steps{
                sh 'docker build -t registry.gitlab.com/northy007/sdp-lab_exam app/'
            }
        }
        stage('Clone Robot repository'){
            agent{
                label 'testNode'
            }
            steps{
                sh 'rm -rf SDP-Lab_exam_robot'
                sh 'git clone https://github.com/SDPP-Group/SDP-Lab_exam_robot.git'
            }
        }
        stage('Run Robot test'){
            agent{
                label 'testNode'
            }
            steps{
                sh 'robot SDP-Lab_exam_robot/exam-robot.robot'
            }
        }
        stage('Push image to a registry')
        {
            agent{
                label 'testNode'
            }
            steps{
                withCredentials([usernamePassword(credentialsId: 'lnwza007', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh 'docker login -u ${USERNAME} -p ${PASSWORD} registry.gitlab.com'
                        sh 'docker push registry.gitlab.com/northy007/sdp-lab_exam'
                }
                sh 'docker rmi -f registry.gitlab.com/northy007/sdp-lab_exam:latest'
            }
        }
        stage('Pull image of simple-api from a registry'){
            agent{
                label 'pre-prodNode'
            }
            steps{
                withCredentials([usernamePassword(credentialsId: 'lnwza007', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh 'docker login -u ${USERNAME} -p ${PASSWORD} registry.gitlab.com'
                        sh 'docker push registry.gitlab.com/northy007/sdp-lab_exam'
                }
                sh 'docker pull registry.gitlab.com/northy007/sdp-lab_exam'
            }
        }
        stage('Create containers of simple-api'){
            agent{
                label 'pre-prodNode'
            }
            steps{
                //sh 'docker stop $(docker ps -q)'
                sh 'docker run -d -p 5000:5000 registry.gitlab.com/northy007/sdp-lab_exam'
            }
        }
    }
}