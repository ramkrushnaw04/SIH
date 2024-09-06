from flask import Flask, request, jsonify
import textExtractor
import os
import chatbot

scriptPath = os.getcwd()
contextPath = os.path.join(scriptPath, 'chatbot/context')

print(contextPath)

app = Flask(__name__)
# app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

@app.route('/')
def home():
    return "Hello, World!"


@app.route('/data', methods=['POST'])
def data():
    content = request.json
    return jsonify(content)


@app.route('/upload', methods=['POST'])
def upload():

    files = request.files
    courseId = request.form.get('courseId') 

    keys = files.keys()

    for key in keys:
        file = files[key]
        extention = file.filename.split('.')[-1]

        binaryData = file.read()
        text = ['', '']

        # print(extention)

        if(extention == 'pdf'):
            print('pdf recieved')
            text = textExtractor.extractTextFromPDF(binaryData)
        
        elif(extention == 'jpeg' or extention == 'jpg' or extention == 'png' or extention == 'webp' or extention == 'gif' or extention == 'bmp' or extention == 'tiff'):
            print('image recieved')
            text = textExtractor.extractTextFormImage(binaryData)
        
        elif(extention == 'pptx'):
            print('pptx recieved')
            text = textExtractor.extractTextFromPPTX(binaryData)
        
        elif(extention == 'docx'):
            print('docx recieved')
            text = textExtractor.extractTextFromDOCX(binaryData)

            
        # saving text in respective course text files
        pathOfCourseContext = os.path.join(contextPath, courseId)
        os.makedirs(pathOfCourseContext, exist_ok=True)

        with open(os.path.join(pathOfCourseContext, 'data.txt') , 'a') as file:
            file.write(text[0] + ' ' + text[1] + ' ')

    return 'ok'



@app.route('/ask', methods=['POST'])
def ansQuestion():
    data = request.get_json()
    courseId = data['courseId']
    question = data['question']

    output = chatbot.getAnswer(courseId, question)

    return jsonify(output)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
