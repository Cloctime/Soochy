import filmdb
from flask import Flask,render_template,jsonify,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')



@app.route('/film', methods=['POST'])
def film():
    titre=request.form['titre']
    result=[]
    c=filmdb.Film(titre)
    result.append(c.getDirector())
    result.append(c.getTitle())
    result.append(c.getActeurs())
    result.append(c.getDuration())
    result.append(c.getDate())
    return render_template("film.html",result=result)


if __name__ == '__main__':
    app.run(
        debug=True
    )
