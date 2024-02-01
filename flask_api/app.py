import os
from flask import Flask, render_template, request,json, jsonify, current_app as app

app = Flask(__name__)

albums_path = os.path.join(app.static_folder, 'data', 'albums.json')

@app.route('/')
def index():
    name = "Team Edge"
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return "<h1>About</h1><p>some other content</p>"

@app.route('/api/v1/albums/all', methods=['GET'])
def api_albums_all():

    #using with allows for opening and closing of file
    with open(albums_path, 'r') as jsondata:
        albums = json.load(jsondata)

    #no need to return an html template
    return jsonify(albums)

@app.route('/api/v1/albums/search', methods=['GET'])
def api_search():

    results=[] #a list to hold our results

    with open(albums_path, 'r') as jsondata:
        albums = json.load(jsondata)

    if 'artist' in request.args:
        artist = request.args['artist']

        for album in albums:

            #print(album[ 'artist'])

            if artist in album['artist']:
                results.append(album)

    if 'year' in request.args:
        year = request.args['year']

        for album in albums:
            #print("year : " + str(album['year']))            
            if (year == str(album['year'])):
                
                print("Match found!")
                results.append(album)

    if 'song' in request.args:

        song_search = request.args['song'].lower()
         
        for album in albums:
            for s in album["songs"]:

                if song_search in s.lower():
                    print("we found a match!!")
                    results.append(album)    
    
    if (len(results) < 1):
        return "Sorry, your query did not find any matches."
    else:
        return (jsonify(results))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2024)
