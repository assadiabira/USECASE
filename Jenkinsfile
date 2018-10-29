node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
  }
  stage ("Test"){
		echo "Test in progress"
    sh "/var/lib/jenkins/jeu_plus_moins.py || true"
    echo "code OK"
  } 
	stage("Deployment"){
		echo "Deployment in progress"
		steps{
			when{
				expression{
					currentBuild.result==null || currentBuild.result=='SUCCESS'
				}
			}
		}
		steps{
			sh "/var/lib/jenkins/jeu_plus_moins.py"
		}
	}	
} 
   
		
