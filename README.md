To run test please perform following steps: 
1. Clone the repo 
2. cd to a folder with docker file
3. For windows in ps console run .\runtests.ps1
or execute commands listed there manually.
Folder 'target' containing report.html will be created in current dir.
For other systems like MacOS two first commands should also work,
and the report might be opened from target folder manually or with corresponding command. 

## Solution description. ##
I used 
1) pytest-bdd framework for implementing human readable tests
2) pytest-html for generating html reports
3) runtests.ps1 contains commands to build a docker image, to rin it, and to open generated html report
4) url is stored in config.yaml
5) basic log messages are added and visible in both console and html report
6) bdd scenarios are located in test/features/get.feature 
There are one datadriven test with two sets of data and one negative test.
7) steps implementation is tests/steps_definitions/test_sample.py
8) helper module contains sample methods for generating data and parsing results.




