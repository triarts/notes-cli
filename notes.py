import sys

def main(args):
	commandDict={
		"docker": [	"SPRING_ENV=test docker compose -f docker-compose-debug.yml up -d --build",
					"docker exec -it asidis_web_1 bash",
					"docker stop $(docker ps -q)",
					"DOCKER_HOST=\"ssh://rancher@10.10.172.30\" SPRING_ENV=test docker compose up -d --build",
					"docker logs -f asidis-web-1 \n     (attach to container live log, from docker compose 'logging: driver:') ",
					"docker exec -it asidis-web-1 bash -c \"echo networkCheckTask | bash TaskRunner.sh\"",
					"docker cp <container-name-or-id>:<container-path> <host-path> \n docker cp asidis-web-1:/home/aisd/data/seat dataDocker/",
					"docker exec -it asidis-web-1 bash -c \"tail -f log/web.log\"",
					],
		"git": ["git checkout -b AL_20240522_1459_asdfasdf",
				"git checkout -",
				"git reset --merge",
				"git rebase --abort",
				"git reset --hard @{u}"
				],
		"bash": ["tail -n 100 -f web.log",
				"scp docker-compose-postgres.yml ata@192.168.100.7:/home/ata/Project/postgresDocker",
				],
		"mvn": ["mvn clean install -Dmaven.test.skip=true",
					"mvn -T 1C install -Dmaven.test.skip=true"
					],
		"java": ["sudo update-alternatives --config java",
					"sudo update-alternatives --config javac"
					],
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
