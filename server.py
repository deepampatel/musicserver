import os
import queue
from flask import Flask, request, render_template,json
from werkzeug.utils import secure_filename

music_dir = 'static/tppp'
music=[]
dirs=os.listdir(music_dir)
for song in dirs:
    music.append(song)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/tppp'
app.config['ALLOWED_EXTENSIONS'] = set(['mp3'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/<filename>')
def song(filename):

    a=('static/tppp/{}'.format(filename))
    return render_template('play.html',
                           title=filename,
                           music_file=a,playlist=json.dumps(music))


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return index()


@app.route('/gg', methods=['POST'])
def uploadpage11():
    return render_template("upload.html")




@app.route('/')
@app.route('/home')
def index():
    music_files1 = [f for f in os.listdir(music_dir) if f.endswith('mp3')]
    music_files_number = len(music_files1)
    return render_template("index.html",
                           title='Home',
                           music_files_number=music_files_number,
                           music_files=music_files1)


if __name__ == '__main__':
    host_self = '127.0.0.1'
    host_remote = 'YOUR IP'
    app.run(host=host_self, port=80)
    # app.run(debug=True)
