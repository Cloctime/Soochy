import filmdb
import os
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

# @app.context_processor
# def override_url_for():
#     return dict(url_for=dated_url_for)
#
# def dated_url_for(endpoint, **values):
#     if endpoint == 'static':
#         filename = values.get('filename', None)
#         if filename:
#             file_path = os.path.join(app.root_path,
#                                  endpoint, filename)
#             values['q'] = int(os.stat(file_path).st_mtime)
#     return url_for(endpoint, **values)

if __name__ == '__main__':
    app.run(
        debug=True
    )
