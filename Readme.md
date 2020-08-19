
Your task is to create the following:
- two python web applications with the following properties:

- application 1:
	- running on port 5000
	- home page with a button/link which takes you to a generate page
	- generation page with route which makes a get request to a route in application 2 for an animal 
	then posts that animal to another route in application 2 which responds with the animal noise.
	Both the animal and their noise then need to be displayed on the web page.

- application 2 (API):
	- running on port 5001
	- no web pages displayed
	- animal route which returns the name of an animal in either text or json form###
	- noise route which takes a given animal and returns their noise in either text or json form###

- these should both be dockerised and tested.

- stretch goals:
	1. deploy your application over multiple VMs with Docker Swarm
	2. add a database layer to your application
	3. achieve 100% unit test coverage for both applications

Hints:
- application 2 is your api, but you can't access it via http://localhost:5000. 
What do you need to change in order to access it through the docker network?