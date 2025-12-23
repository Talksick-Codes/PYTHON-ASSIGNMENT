
###Create a file called input.txt and write at least five lines of text into it.
#Write a Python script to:
#Read the contents of input.txt.
#Count the number of words in the file.
#Convert all text to uppercase.
#Write the processed text and the word count to a new file called output.txt.
#Print a success message once the new file is created.
with open("task.txt","r") as file:
    content=file.read()
    count=len(content.split())
    upper_case_content=content.upper()
with open("output.txt","w") as file:
    file.write(upper_case_content)
    file.write(f"\n Word Count:{count}")
    print("SUCCESS")