from flask import Flask, render_template, request, url_for
from forms import ClubSearchForm
import sqlite3
app = Flask(__name__)

# App config
# DISABLE THE LINE UNDERNEATH BEFORE PUSHING TO PRODUCTION
app.env = 'development'
db = 'clubs.db'
conn = sqlite3.connect(db)
c = conn.cursor()
club_data_arr = c.execute('SELECT * FROM clubs ORDER BY name')
data = {}
for entry in club_data_arr:
    data[entry[0]] = (entry[1], entry[2])

@app.route('/')
@app.route('/index')
def welcome():
    # Change link to /clubs for clubs
    return render_template('index.html')

@app.route('/clubs', methods=['GET','POST'])
def clubs_selector():
    search = ClubSearchForm(request.form)
    search_string = search.data['search'].strip().lower()
    club_data = {}
    if request.method == 'POST':
        for name, value in data.items():
            url = value[0]
            descr = value[1]
            if search_string != '':
                if any(search_string in field for field in (name, url, descr)):
                    club_data[name] = url
            else:
                club_data[name] = url
    else:
        for name, value in data.items():
            url = value[0]
            # descr = value[1]
            club_data[name] = url

    return render_template('clubs.html', form=search, club_data=club_data)

@app.route('/hour-tracker')
def hour_tracker():
    return render_template('hour-tracker.html')

def main():
    # Runs on localhost:8080 in 'debug' mode. app gets reloaded every time
    # changes are made to the app.
    app.run(host='127.0.0.1', port=8080, debug=True)

if __name__ == '__main__':
    # Run Flask app
    main()