import recover,filmdb
from flask import Flask,render_template,jsonify,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('research.html')


@app.route('/selectListe')
def selectListe():
    return render_template('selectListe.html')



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


@app.route('/liste',methods=['POST'])
def liste():
    titres=[]
    if request.method=='POST':
        if request.form['page']=='page jaime':
            l=recover.recover("jaime")
            titres=[]
            for film in l.getListe():
                titres.append(film.getTitle())
        if request.form['page']=='page jaime pas':
            l=recover.recover("jaimepas")
            titres=[]
            for film in l.getListe():
                titres.append(film.getTitle())
        return render_template("liste.html",result=titres)

if __name__ == '__main__':
    app.run(
        debug=True
    )
