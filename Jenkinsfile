node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
	}
  stage ("Test"){
    echo "Test in progress"
    sh "php -l /var/lib/jenkins/Usecase/consultation_mysql.php"
		post{
			succes{
	 			echo "Code Ok"
			}
		}
  } 	
	//stage ("Deployment"){
	//sh "php /var/lib/jenkins/Usecase/consultation_mysql.php"
	//junit "/var/lib/jenkins/Usecase/report.xml"
	//}
} 
   
		
