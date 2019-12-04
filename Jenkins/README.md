## Call a job
``` groovy
def build = build job: '/path/to/job',
    parameters: [
		string(name: 'STRING_PARAM', value: 'value'), 
		text(name: 'TEXT_PARAM', value: 'multiline\ntext\n'),
		booleanParam(name: 'BOOLEAN_PARAM', value: false)
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
## Clone repo
