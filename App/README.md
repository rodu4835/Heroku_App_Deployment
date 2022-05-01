README For Team 3 Heroku App Deployment

Hopefully you have been added to the collaborator list on Heroku

In order to update to heroku,
navigate in your command line to this Heroku Folder
make sure to connect the folder to the heroku app
works best if you pull the Heroku folder out into another location on your drive as the gits will get confused

	git init
	heroku git:remote -a consolewar
	
	make your changes
	
	git add .
	git commit -m 'your message'
	git push heroku master
	
	check out the page
	
	https://consolewar.herokuapp.com/
	
	
Files in this directory
	- Main project files
		index.html
		index.css
		JSWar.js
	- Files needed to run on Heroku
		composer.json
		index.php