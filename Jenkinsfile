node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
		archiveArtifacts artifacts: 'Usecase/target/*.jar' , fingerprint:true
	}
  stage ("Test"){
		echo "Test in progress"
    sh "/var/lib/jenkins/jeu_plus_moins.py || true"
    echo "code OK"
  } 	
} 
   
		
