def JenkinsBuildTest():
    result={}
    for i in range(20):
        result[i]="test -"+str(i)
    return result

def JenkinsBuildDeploy():
    result={}
    for i in range(10):
        result[i]="deploy -"+str(i)
    return result


if __name__ == '__main__':
    print(JenkinsBuildTest())
    print(JenkinsBuildDeploy())