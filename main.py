from flask import Flask, render_template
from flask import request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def submit():
    if request.method == 'POST':
        s = request.files['audio']
        s.save(r'/home/saurabh/PycharmProjects/audio_summariser/resources/received_audio/audio_file.wav')
    os.system('python3 /home/saurabh/PycharmProjects/audio_summariser/modules/audio_denoise/denoiser.py')
    os.system('python3 /home/saurabh/PycharmProjects/audio_summariser/modules/speech_to_text/speech_to_text.py')
    os.system('python3 /home/saurabh/PycharmProjects/audio_summariser/modules/text_punctuator/text_punctuator.py')
    os.system('python3 /home/saurabh/PycharmProjects/audio_summariser/modules/text_summariser/summarizer.py')
    file_name = r'/home/saurabh/PycharmProjects/audio_summariser/resources/punctuated_text/punct_text.txt'
    file = open(file_name)
    line = file.read()
    file.close()
    return render_template("result.html", text=line)

if __name__ == "__main__":
    app.run(debug=True)
