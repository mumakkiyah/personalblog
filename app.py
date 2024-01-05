from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# main app path 
# loading the titles from a list for testing only
@app.route("/")
def main_index():
    titles = ['The art of understanding critisism', 'Where did all the wild things to?', 'Where does our motivation come from?']
    return render_template('home.html', titles=titles)

# list of posts page
# loaded from a list for testing only
@app.route("/archive")
def post_archive():
    posts = ['The art of understanding critisism','Where did all the wild things to?','Where does our motivation come from', 'Learning from the past', 
             'De-risk projects without compromises', 'When you don''t start with WHY', 'When calorie macros matter', 'Why did the chicken cross the road?', 
             'My music taste evolution', 'A PM''s guide to finding peace', 'When is enough is enough', 'Focus on what matters most']
    return render_template('archive.html', posts=posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)