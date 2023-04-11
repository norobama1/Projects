import openai
import PyPDF2

# Open the PDF file
with open(r"C:/Users/KIIT\Downloads/Profile.pdf", 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)


    # Extract text from each page of the PDF
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Close the PDF file
    file.close()
# Print the extracted t

# Set up OpenAI API credentials
openai.api_key = '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'

# Use OpenAI to ask questions
question = 'College name?'
generated_text = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f'Q: {question}\nText: {text}\nA:',
    max_tokens=1024
)
answer = generated_text.choices[0].text.strip()

# Print the generated answer
print('Answer:', answer)