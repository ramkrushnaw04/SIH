## WORKING

- Extract text from input files  
- Save this extracted text in a text file in respective folder of the course (folders are named by courseId)
- When a question is asked, we sent the context file along with the question to LLM and get the output

## API ENDPOINTS  
- ### /upload
      {
            courseId: Integer,
            file: ( pdf,  jpeg,  pptx )
      }

- ### /ask
      {
            courseId: Integer,
            question: String
      }
      
## TODO
- Add more formats for input files (doc, docx, ppt, png, jpg, wepb)
- Send only necessary part of the context insted of the whole thing
