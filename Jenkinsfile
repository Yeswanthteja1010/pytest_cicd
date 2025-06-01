pipeline{
  agent any
  
  stages{
    stage('set the environment')
    {
      steps{
        sh '''
      python3 -m venv .venv
      . .venv/bin/activate
      pip install --upgrade pip
      pip install -r requirements.py
      pip install pytest coverage
      '''
      }
    }
    stage('run tests with pytest')
    {
      steps{
        sh '''
        . .venv/bin/activate
        pytest tests/
      '''
      }
    }
    stage('generate coverage report')
    {
      steps{
        sh'''
        . .venv/bin/activate
        coverage run -m pytest tests/
        coverage report
        coverage html
      '''
      }
    }
    stage('publish coverage report') 
    {
      steps{
        publishHTML(target: [
          reportDir: 'htmlcov',
          reportFiles: 'index.html',
          reportName: 'code coverage report',
        ])
      }
      
    }
  }
  post{
    always{
      echo 'cleaning the environment'
      sh 'rm -rf .venv'
    }
  }
}
