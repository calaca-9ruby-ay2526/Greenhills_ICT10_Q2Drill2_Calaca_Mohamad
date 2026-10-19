from pyscript import document, display

def get_name(e):
    document.getElementById('div1').innerHTML = ''
    first_name = document.getElementById('fname').value
    last_name = document.getElementById('lname').value
    full_name= first_name + last_name

    grade_7_members = {'Abdullah Ibrahim', "Austin Maneja"}
    grade_8_members = {'Kyryll Chudomirovich Flins', 'diluc'}
    grade_9 = {'Dania'}
    grade_10 = {'Pocholo'}

    members = (grade_7_members | grade_8_members | grade_9 | grade_10)
    members.add(full_name)
    

    
   

    display(f'List of members {members} amount of members {len(members)}', target='div1')

