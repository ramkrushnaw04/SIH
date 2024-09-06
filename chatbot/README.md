## WORKING

- Extract text from input files  
- Save this extracted text in a text file in respective folder of the course (folders are named by courseId)
- When a question is asked, we sent the context file along with the question to LLM and get the output

## API ENDPOINTS  
- ### /upload
      {
            courseId: Integer,
            file: ( jpeg,  jpg,  png,  gif,  bmp,  tiff,  webp,  pdf,  pptx )
      }

- ### /ask
      {
            courseId: Integer,
            question: String
      }
      
## TODO
- Add more formats for input files (doc, docx, ppt) - 
- Send only necessary part of the context insted of the whole thing


## UPDATES
06/09/2024
- Added support for jpg, png, webp, bmp, tiff, docx, gif  
- No longer working on legacy formats doc and ppt as they are obsolete.