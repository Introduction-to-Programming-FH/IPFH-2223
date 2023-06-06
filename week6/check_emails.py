import re
def check_emails(dictionary_of_emails):
    correct_emails = []
    for name in dictionary_of_emails:
        for email in dictionary_of_emails[name]:
            if re.match(r"^[a-zA-Z0-9._%+-]+@lmu.de$", email) or re.match(r"^[a-zA-Z0-9._%+-]+@dkes.fak12.lmu.de$", email):
                correct_emails.append(email)
    return correct_emails

input_dict = {"Bruno":["hello@lmu.de", "hi@gmail.com", "yes@dkes.fak12.lmu.de"], "John":["john@live.it", "johnlive.it", "john@lmu.de"]}
print(check_emails(input_dict))