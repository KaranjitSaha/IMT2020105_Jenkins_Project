pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/RBang2501/IMT2020105_Jenkins_Project.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Maximum.py"
                sh "./Maximum.py"
            }
        }
        stage('Test Code Passed') {
            steps {
                sh "chmod u+x Pass_test_case.py"
                sh "./Pass_test_case.py"
            }
        }
        stage('Test Code Failed') {
            steps {
                sh "chmod u+x Fail_test_case.py"
                sh "./Fail_test_case.py"
            }
        }
    } 
}
