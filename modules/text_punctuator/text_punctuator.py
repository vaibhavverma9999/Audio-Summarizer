from punctuator import Punctuator
p = Punctuator(r'/home/saurabh/PycharmProjects/audio_summariser/modules/text_punctuator/INTERSPEECH-T-BRNN.pcl')
file_name = r'/home/saurabh/PycharmProjects/audio_summariser/resources/transcripted_text/text.txt'
file = open(file_name)
line = file.read()
file.close()
punctuated_line = p.punctuate(line)
output_text_file_name = r'/home/saurabh/PycharmProjects/audio_summariser/resources/punctuated_text/punct_text.txt'
text_file = open(output_text_file_name, "wt")
text_file.write(punctuated_line)
text_file.close()
