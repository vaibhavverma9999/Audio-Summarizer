import speech_recognition as sr

filename = r'/home/saurabh/PycharmProjects/audio_summariser/resources/cleaned_audio/cleaned_file.wav'
output_text_file_name = r'/home/saurabh/PycharmProjects/audio_summariser/resources/transcripted_text/text.txt'
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    text_file = open(output_text_file_name, "wt")
    text_file.write(text)
    text_file.close()


