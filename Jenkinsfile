node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
		archiveArtifacts artifacts: '/var/lib/jenkins/Usecase/archives_usecase.jar' , fingerprint:true
	}
  stage ("Test"){
		echo "Test in progress"
    sh "/var/lib/jenkins/Usecase/jeu_plus_moins.py || true"
    echo "code OK"
  } 	
} 
   
		
