node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
	}
  stage ("Test"){
    echo "Test in progress"
    sh "php -l /var/lib/jenkins/Usecase/consultation_mysql.php"
		archiveArtifacts artifacts: '/var/lib/jenkins/Usecase/*.jar', fingerprint: true
  } 	
	stage ("Deployment"){
		sh "php -f /var/lib/jenkins/Usecase/consultation_mysql.php" 
	} 
}
		
