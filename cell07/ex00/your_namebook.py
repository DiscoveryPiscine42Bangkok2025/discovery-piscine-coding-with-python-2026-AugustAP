#!/usr/bin/env -S python3

def array_of_names(persons):
    names = []
    for first_name, last_name in persons.items():
        whole_name = first_name.capitalize() + " " + last_name.capitalize()
        names.append(whole_name)
    return names

persons = {
    "jean" : "valjean",
    "grace" : "hopper",
    "xavier" : "niel",
    "fifi" : "brindacier"
}

print(array_of_names(persons))