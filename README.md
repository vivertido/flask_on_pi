## Flask on the Pi

This repo contains 3 examples of using Flask, for use in Term 1 of Code Next's Team Edge program, a course that includes Full Stack Web deveolpment with Flask primarily using the Raspberry Pi.

### Projects Include:

- Hello Flask( a basic template for serving raw html).
- Flask-API( an example of using Flask to serve API content with endpoints)
- Flask-PG ( A playground app with different pages, including the NASA API Picture of the Day and other examples of using Flask)
- Code Next ( The static [codenext](https://codenext.withgoogle.com) website recreated in a Flask app )

### Usage:
The Majority of the projects are simple but one requires a Raspberry Pi, as it reads system data and disiplays it on a page. These are basic examples meant to inspire the creation of your own apps. 

- Clone the projects to your Pi Desktop or other folder:
```bash
 $ cd ~/Desktop
 $ git clone https://github.com/vivertido/flask_on_pi.git

```
To run an app, navigate to its folder and run:
```bash
 $ python3 app.py

```
You can also run the app directly from many coding IDEs like VSCode.

### TODOs:
- Explore how Hello Flask works and how the files are structured.
- Explore app.py and how each page, or route is served.
- Start with the Hello Flask and add more pages/routes. Add buttons or links so you can navigate to and from these new pages.
- Use render_template to load HTML pages stored in templates folder and link CSS as needed.
- Explore the Playground projects. What else would you display on a Flask app? Bring in a project you already worked on and incorporate it. This can be your "Porfolio" project.
- Use the Playground `dynamic.html` example to see how to use Jinja to render dynamic content, and how `app.py` serves this.
- Explore how to Fetch fresh daily data from a 3rd party API (Nasa Picture of the Day) into a page. Hint, you will want to get an API Key of your own for this [here](https://api.nasa.gov/). What other API data can you fetch and load?
- Try the Flask API project to explore how build endpoints for your own APIs so others can call your app to serve up content by reading the parameters in a Fetch URL with queries. There is some JSON data already in the `data` folder for you to serve up, or get your own.
- Have fun building with Flask!
  
