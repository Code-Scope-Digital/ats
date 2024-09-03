import re
import os
import PyPDF2
from docx import Document

def read_file(file_path):
    # Get the file extension
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == ".pdf":
        return read_pdf(file_path)
    elif ext == ".docx":
        return read_docx(file_path)
    else:
        raise ValueError("Unsupported file type: " + ext)

def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)

# Example usage:
resume_text = read_file("/Users/priyanshupriyam/Desktop/Personal/ATS/Resume Priyanshu Priyam.pdf")  # or "sample.docx"
print(resume_text)


# Sample job description (in a real ATS, this would be more dynamic)
job_description = """
Looking for a software developer proficient in Python, Java, and SQL.
Experience with cloud platforms like AWS and Azure is a plus.
Strong problem-solving skills and ability to work in a team.
"""

# Keywords extracted from the job description
job_keywords = ["Python", "Java", "SQL", "AWS", "Azure", "problem-solving", "teamwork"]

# Sample resume (in real ATS, this would be parsed from a file or a database)
# resume_text = """
# John Doe
# Email: john.doe@example.com
# Phone: 123-456-7890

# Skills:
# - Programming: Python, C++, SQL
# - Cloud Platforms: AWS, Google Cloud
# - Teamwork, Leadership, Communication

# Experience:
# - Software Developer at TechCorp (2019-Present)
# - Developed backend services using Python and SQL.
# - Worked on cloud integration with AWS.
# - Collaborated with a team of developers to solve complex problems.

# Education:
# - BSc in Computer Science from XYZ University (2015-2019)
# """

# Function to match resume against job keywords
def score_resume(resume_text, job_keywords):
    # Convert resume to lowercase and split into words for matching
    resume_words = re.findall(r'\w+', resume_text.lower())
    print(resume_words)
    
    # Initialize score
    score = 0
    
    # Match keywords
    for keyword in job_keywords:
        # Convert keyword to lowercase for case-insensitive matching
        if keyword.lower() in resume_words:
            score += 1  # Increase score if keyword is found

    # Return the match score
    return score

# Function to extract contact information
def extract_contact_info(resume_text):
    # Simple regex to find email and phone number (this can be expanded for more complex parsing)
    email = re.search(r'[\w\.-]+@[\w\.-]+', resume_text)
    phone = re.search(r'\+\d{2}-\d{10}', resume_text) or re.search(r'\+\d{2}\d{10}', resume_text) or re.search(r'\d{10}', resume_text)
    
    # Return contact information if found
    return {
        "Email": email.group(0) if email else "Not Found",
        "Phone": phone.group(0) if phone else "Not Found"
    }

# Score the resume
resume_score = score_resume(resume_text, job_keywords)

# Extract contact information
contact_info = extract_contact_info(resume_text)

# Print the results
print("Resume Score:", resume_score, "out of", len(job_keywords))
print("Contact Information:", contact_info)