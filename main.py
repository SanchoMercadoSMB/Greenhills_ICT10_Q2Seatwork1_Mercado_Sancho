#Student Ict club member checker
from pyscript import display, document

def student_club(e):
    document.getElementById("output").innerHTML = ''

    lastname = document.getElementById("last_name").value
    firstname = document.getElementById("first_name").value

    ICT_members = [('Darren', 'Watkins'), ('Rob', 'Dillingham'), ('Joshua', 'Ortiz'), ('Kristine', 'Pasco')]

    member_checker = (firstname.lower(), lastname.lower()) in ICT_members

    display_message = [
    f'Sorry {firstname} {lastname}, your name is not on the list.',
    f'Congratulations, {firstname} {lastname}! You are now part of the ICT club. SO TUFF!!'
]

    display(display_message[member_checker], target="output")