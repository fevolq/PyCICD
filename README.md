# 介绍
用于 CI/CD 测试

# Jenkins
## 内部部署
需要在 jenkins 所在服务器安装 python 解释器
* app 应用
```
pipeline {
	agent any

	stages{
		stage("pull codebuild checkout") {
			steps {
				git branch: "main", url: "https://github.com/fevolq/PyCICD.git"
			}
		}

		stage("setup environment") {
			steps {
				sh "python3 -m venv venv"
				sh ". venv/bin/activate && pip install -r requirements.txt"
			}
		}

		stage("start project") {
			steps {
			    script {
			        def startCmd = '. venv/bin/activate && uwsgi -d --ini app.ini'
			        def reloadCmd = '. venv/bin/activate && uwsgi --reload app.pid'
			        def reloadResult = sh script: reloadCmd, returnStatus: true
			        
			        if (reloadResult == 0) {
			            echo 'Reload successful.'
			        } else {
			            echo 'Reload failed. Starting the project...'
			            sh script: startCmd
			            echo 'Started successful.'
			        }
			    }
			}
		}
	}
}
```
* 脚本
```
pipeline {
	agent any

	stages{
		stage("pull codebuild checkout") {
			steps {
				git branch: "main", url: "https://github.com/fevolq/PyCICD.git"
			}
		}

		stage("setup environment") {
			steps {
				sh "python3 -m venv venv"
				sh ". venv/bin/activate && pip install -r requirements.txt"
			}
		}

		stage("start project") {
			steps {
				sh ". venv/bin/activate && python script.py"
			}
		}
	}
}
```
<img alt="结果" src="./assess/jenkins_script.png" width="500"/>