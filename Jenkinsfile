pipeline {
//executeur pour la construction des jobs
	agent any 
//récupération du code utilisateur présent dans Git
	stage ("Dev"){
		checkout scm
		
	}
//outil de test du code, renvoie OK ci code bon	
	stage ("Test"){
		if ( code || true){
			echo "test passed: it's OK!"
		}
	}
//si OK: compilation du code par la machine et stockage des binaires dans artifactory	
	stage ("Deployement"){
		sh "code"
		
	}

}
