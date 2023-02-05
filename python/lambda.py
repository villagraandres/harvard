people=[
    {"name":"Liam","band":"Oasis"},
    {"name":"Noel","band":"Oasis"},
    {"name":"Damon","band":"Blur"}

]


people.sort(key=lambda person: person['name']);  

print(people);