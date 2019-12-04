## Call a job
``` groovy
build job: '/TConstructor/Build/merge-git-branches',
    parameters: [
        string(name: 'SOURCE_BRANCH', value: 'base/develop'), 
        string(name: 'DESTINATION_BRANCH', value: 'base/build-develop')
    ]
```

## Clone repo
