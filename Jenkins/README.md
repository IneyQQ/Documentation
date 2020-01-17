## Call a job
``` groovy
def build = build job: '/path/to/job', wait: true, propagate: true,
    parameters: [
        string(name: 'STRING_PARAM', value: 'value'), 
        text(name: 'TEXT_PARAM', value: 'multiline\ntext\n'),
        booleanParam(name: 'BOOLEAN_PARAM', value: false),
        [$class: 'LabelParameterValue', name: 'NODE', label: 'NodeLabel']
    ]
echo build.displayName
```
## Set display name
```groovy
currentBuild.displayName = "${currentBuild.displayName} 43215"
```
## Send email
```groovy
emailext subject: "Build Failure",
    from: "Jenkins",
    to: "adam@paradise.home,eva@hell.out",
    body: "Multiline\ntext\n"
```
## Try/catch/finally
```groovy
try {
    throw new Exception("Bad thing happens")
} catch (err) {
    fixIfNeeded()
    throw new Exception(err)
} finally {
    freeResources(resources)
}
```
## Skip stage
```groovy
when {
    equals expected: 1, actual: 2
}
```
## Clone Git repo
```groovy
environment {
    GIT_CREDENTIALS_ID = 'CredsId'
    GIT_TOKEN = credentials('APIToken')
    GIT_URL_WITH_TOKEN = "https://x-token-auth:$GIT_TOKEN@github.com/IneyQQ/project"
    GIT_SSH = 'git@github.com:IneyQQ/project'
    PROJECT_DIR = 'project'
}

agent {
    docker {
        label 'NodeLabel'
        image 'samueldebruyn/debian-git'
    }
}

dir(PROJECT_DIR) {
    checkout changelog: true, poll: false, scm: [
        $class: 'GitSCM',
        branches: [[name: "${params.BRANCH1}"], [name: "${params.BRANCH2}"]],
        doGenerateSubmoduleConfigurations: false,
        extensions: [[$class: 'LocalBranch', localBranch: "**"]],
        submoduleCfg: [],
        userRemoteConfigs: [[
            url: "${env.GIT_SSH}",
            credentialsId: "${env.GIT_CREDENTIALS_ID}",
            name: "origin"
        ]]
    ]
    sh """
    git remote set-url origin $GIT_URL_WITH_TOKEN
    git config --global user.email "IneyQQ@gmail.com"
    git config --global user.name "Iney QQ"
    """
}
```
## Merge Git branches
```groovy
sh """
    git checkout ${SOURCE_BRANCH}
    git checkout ${TEMP_BRANCH}
"""
def mergeOutput = sh returnStdout: true, script: "git merge ${SOURCE_BRANCH} --no-ff"
println mergeOutput
if (mergeOutput.contains("Already up-to-date.")) {
    env.MERGE_UP_TO_DATE = "y"
    return
} else {
    env.MERGE_UP_TO_DATE = "n"
}
sh 'git push'
```
## Get value from xml
```groovy
env.BUILD_VERSION = sh(returnStdout: true, script: "cat pom.xml | grep -oPm1 '(?<=<version>)[^<]+'").trim()
```
## Push Git if there are changes
```groovy
sh """
    changes=`git status --porcelain`

    if [ -z "$changes" ]; then
        echo "No changes..."
    else
        git add .
        git commit -m "Commit"
		git push
    fi
"""
```
## Git merge without a file
```bash
git checkout ${BRANCH1}
git checkout ${BRANCH2}

set +e
git merge ${BRANCH1}
set -e

git reset HEAD -- ${FILE1}
git checkout --ours ${FILE1}

not_merged=(\$(git diff --name-only --diff-filter=U))
if [ \${#not_merged[@]} != 0 ]; then
    git diff --diff-filter=U
    exit 1
fi
```
## Run Sonar
// Run sonar scanner to collect data
withSonarQubeEnv('SonarQube') {
    sh """
    export MAVEN_OPTS="-Xmx5120m"
    mvn sonar:sonar
    """
}
// Wait at least for 1 minutes while server analysing code
timeout(time: 1, unit: 'MINUTES') {
    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
    // true = set pipeline to UNSTABLE, false = don't
    waitForQualityGate abortPipeline: true
}
## Run Kubectl
withKubeConfig([credentialsId: 'KuberConfig']) {
    sh """
    set +e
    kubectl delete -f pleaseDeleteIt.yaml
    """
}