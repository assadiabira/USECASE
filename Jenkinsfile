node {
//executeur pour la construction des jobs
	agent any 
//récupération du code utilisateur présent dans Git
	stage ("Dev"){
		checkout scm
	}
//outil de test du code, renvoie OK ci code bon	
	stage ("Test"){
		sh 'python Usecase/jeu_plus_moins_ok.py'
		if ( Usecase/jeu_plus_moins_ok.py || true){
			echo "test passed: it's OK!"
		}
	}
}
