INSTRUCTIONS:

setting up the environment + initiating the database 
1. boot up vagrant with command "vagrant up" in the vagrant folder
2. access vagrant using the command "vagrant ssh"
3. change folder using cd /vagrant
4. open postgre sql command line by typing command "psql"
5. load the database scheme / initialization file by typing "\i tournament/tournament.sql"
6. leave postgre sql command line by typing "\q" or pressing "control-d" on Mac OS X
7. if you don't continue to running tests or the main file, shut down vagrant using the command "vagrant halt"


running tests:
0. prerequisite: you need to perform te setting up the envirotnment + initiating the database (see points above)
1. boot up vagrant with command "vagrant up" in the vagrant folder
2. access vagrant using the command "vagrant ssh"
3. change folder using cd /vagrant
4. run the test file by typing "python tournament/tournament_test.py"
5. you will see in your terminal prints our the statuses of invidividual tests
6. if you don't continue to running the main file, shut down vagrant using the command "vagrant halt"


running the main file tournament.py:
0. prerequisite: you need to perform te setting up the envirotnment + initiating the database (see points above)
1. boot up vagrant with command "vagrant up" in the vagrant folder
2. access vagrant using the command "vagrant ssh"
3. change folder using cd /vagrant
4. run the test file by typing "python tournament/tournament.py"
5. by default, you will see only an output of the swisspairings function. If you haven't run the tournament_tests.py file before, it will return an empty array, because no players or matches are initialized in the tournament.py file. You can un-comment the commands on the bottom of the line to run more tests from this file
6. if you don't continue to running the main file or tests, shut down vagrant using the command "vagrant halt"