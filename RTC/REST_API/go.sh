#
# OSLC REST API living example
#
# You can use script user to login and check results.
#

USER=fmercury
PASS=tEu0NVH
COOKIES=.cookies

# Create empty cookies
curl -k -c $COOKIES https://jazz-lsbt.iba:9443/ccm/authenticated/identity
# Log in and save cookies
curl -k -L -c $COOKIES -b $COOKIES -d j_username=$USER -d j_password=$PASS https://jazz-lsbt.iba:9443/ccm/authenticated/j_security_check
# Get projects
curl -k -b $COOKIES https://jazz-lsbt.iba:9443/ccm/oslc/workitems/catalog
# Get workitems from project with UUID="_Ex29cHLqEeib7oT4_6AGzA"
curl -k -H "Accept: application/rdf+xml" -b $COOKIES https://jazz-lsbt.iba:9443/ccm/oslc/contexts/_Ex29cHLqEeib7oT4_6AGzA/workitems
# Create new task from newtask.rdf file
curl -k -b $COOKIES -H "Content-Type: application/rdf+xml" -H "OSLC-Core-Version: 2.0" -X POST -d @newtask.rdf https://jazz-lsbt.iba:9443/ccm/oslc/contexts/_Ex29cHLqEeib7oT4_6AGzA/workitems/task
# Create new task from newtask.json file
curl -k -b $COOKIES -H "Content-Type: application/json" -H "OSLC-Core-Version: 2.0" -X POST -d @newtask.json https://jazz-lsbt.iba:9443/ccm/oslc/contexts/_Ex29cHLqEeib7oT4_6AGzA/workitems/task

