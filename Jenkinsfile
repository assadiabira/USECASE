node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
	}
  stage ("Test"){
    echo "Test in progress"
    sh "php -l /var/lib/jenkins/Usecase/consultation_mysql.php"
  } 	
	stage ("Deployment"){
		sh "make /var/lib/jenkins/Usecase/consultation_mysql.php" 
	} 
}
		
