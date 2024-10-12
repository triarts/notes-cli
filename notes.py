import sys

def main(args):
	commandDict={
		"docker": [	"SPRING_ENV=test docker compose -f docker-compose-debug.yml up -d --build",
					"docker exec -it asidis_web_1 bash",
					"docker stop $(docker ps -q)",
					"DOCKER_HOST=\"ssh://rancher@10.10.172.30\" docker compose up -d --build",
					"docker logs -f asidis-web-1 \n (attach to container live log, from 'logging: driver:') ",
					],
		"git": ["git checkout -b AL_20240522_1459_asdfasdf",
				"git checkout -",
				"git reset --merge",
				"git rebase --abort"
				],
		"bash": ["tail -n 100 -f web.log",
				"scp docker-compose-postgres.yml ata@192.168.100.7:/home/ata/Project/postgresDocker",
				],
		"mvn": ["mvn clean install -Dmaven.test.skip=true"],
		"liquibase": [	"mvn liquibase:update",
						"mvn liquibase:update -Dliquibase.toTag=1.2",
						"mvn liquibase:rollback -Dliquibase.rollbackTag=1.1",
						"mvn liquibase:clearCheckSums"
						],
	}

	userInput = list(args)
	if len(userInput) == 0:
		for key in commandDict:
			print(key)
	else:
		for val in commandDict[userInput[0]]:
			print(val)

if __name__ == "__main__":
    main(sys.argv[1:])
