# Webservice_template  
This is the template for all new services. 

In order to adapt to our deployment in docker, we changed the default file directory of django：

		-We put the 'database' and 'static folders (.js, .cc, image)' in the Ai_Django_WebService folder.
			-'Ai_Django_WebService folder' will serve as a shared volume for the docker container.
		-We added 'Dockerfile' and 'requirements.txt' to the root directory.

In each use, it is recommended to create a new branch according to the template to expand your own functions.

