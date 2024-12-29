class Person:
    people = {}

    def __init__(self, name, age):

        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self

    def __repr__(self):

        spouse_info = f", Spouse: {self.spouse.name}" if self.spouse else ""
        return f"Person(Name: {self.name}, Age: {self.age}{spouse_info})"


def create_person_list(people_data):
    for person in people_data:
        name = person["name"]
        age = person["age"]
        Person(name, age)

    for person in people_data:
        name = person["name"]
        spouse_name = person.get("wife") or person.get("husband")
        if spouse_name:
            Person.people[name].spouse = Person.people.get(spouse_name)

    return list(Person.people.values())