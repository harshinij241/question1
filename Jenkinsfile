pipeline{
    agent any

    stages{
        stage('Checkout'){
            git branch : 'main', url : 'https://github.com/harshinij241/question1'
        }

        stage('Install dependencies'){
            bat 'pip install -r requirements.txt'
        }

        stage('Running unit test'){
            bat 'python -m pytest test_app.py'
        }
    }
    post{
        success{
            echo 'Success'
        }
        failure{
            echo 'Failure'
        }
    }
}
