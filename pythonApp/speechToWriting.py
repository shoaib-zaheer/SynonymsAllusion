import speech_recognition as sr
# initialize the recognizer
r = sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:
    # read the audio data from the default microphone
    r.adjust_for_ambient_noise(source)
    audio_data = r.listen(source, None, 5) #, duration=duration

    print("Recognizing...")
    # convert speech to
try:
    text = r.recognize_google(audio_data)
    # text = r.recognize_google(audio_data, language="es-ES") # for other languages
    print('Do you mean : {}'.format(text))
except:
    # if it is not listening well
    # sr.UnknownValueError as e:
    print('Sorry could you repeat your sentence')
# writing text in to a text file and save it in a location
with open('./textFiles/speech.txt', 'a') as f:
    f.writelines(text)

# sarching for string in a file
def search_string_in_file('/home/afg/Documents/ART-MY/New-project-ids/SecondYear/synonymsAllusion/pythonApp/speech.txt',text):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open('/home/afg/Documents/ART-MY/New-project-ids/SecondYear/synonymsAllusion/pythonApp/speech.txt', 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if text in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))

    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results
