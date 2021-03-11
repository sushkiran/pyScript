"""
When we want to send the same invitations to many people, the body of the mail does not change.
Only the name (and maybe address) needs to be changed. Mail merge is a process of doing this.
Instead of writing each mail separately, we have a template for body of the mail and a list of names
that we merge together to form all the mails.

1. Create a text file “names.txt” having the names.
2. Create a text file “body.txt” having the body of email.
3. Write a program which should create separate files after picking names from names.txt.
"""

with open('body.txt', 'r') as f_body:
    body = f_body.read()

with open("names.txt", "r") as f_name:
    for name in f_name:
        name = name.strip().capitalize()
        file = open(name + '.txt', 'w')
        file.write(body.format(name))
        file.close()


print('Done')