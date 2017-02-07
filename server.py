import os
from flask import Flask, request, render_template
from werkzeug import secure_filename

music_dir = 'static/tppp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/tppp'
app.config['ALLOWED_EXTENSIONS'] = set(['mp3'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/<filename>')
def song(filename):
    return render_template('play.html',
                           title=filename,
                           music_file=filename)


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
    music_files = [f for f in os.listdir(music_dir) if f.endswith('mp3')]
    music_files_number = len(music_files)
    return render_template("index.html",
                           title='Home',
                           music_files_number=music_files_number,
                           music_files=music_files)


if __name__ == '__main__':
    host_self = '127.0.0.1'
    host_remote = '192.168.43.231'
    app.run(host=host_remote, port=80)
    # app.run(debug=True)
