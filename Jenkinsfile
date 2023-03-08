node {
    stage('Git Pull') {
        git 'https://github.com/maksimTrs/pythonSeleniumWDProject1'
     }
    stage('Python Project Build') {
        bat 'pytest tests/ -v -s --browser_name="%browserName%" --URL="%url%"'
     }
    stage('Reports Generation') {
        allure includeProperties: false, jdk: '', results: [[path: 'target/allure-results']]
        emailext attachLog: true, body: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!<br>Visit ${BUILD_URL} URL  to observe more details', subject: 'Pipeline Build [Pipeline1 for Projects] was finished', to: 'hokagemax@gmail.com'
     }

}