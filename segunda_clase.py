
class Alumno() :
    def __init__(self, name, surname, comision):
        self.name = name
        self.surname = surname
        self.comision = comision
        self.subjects = {"matematica": [], "programacion": [], "fisica" : []}
    
    def introduction(self) :
        print(f"Hola soy {self.name} {self.surname} y soy parte de la comision {self.comision}")


    def add_notes(self, subject, note) :
        """ 
        Si la materia existe en el diccionario se agregará al array interno como una nueva nota
        """
        if subject in self.subjects :
            if len(self.subjects[subject]) <= 3 :
                self.subjects[subject].append(note)


    def show_promedy(self):
        """
        Se recorre el diccionario con .items() en donde sub es la clave ("matematica")
        y note es el valor correspondiente, en este caso cada array de  notas.
        Esto actuliza subjects que ya se inicializa al momento de crear un objeto Alumno()
        """
        for sub, note in self.subjects.items() :
            final = sum(note)
            cant = len(note)
            if cant != 0 :
                print(f"Mi nota final en {sub} es {final / cant}")
            else :
                print(f"No tengo notas para la materia {sub}")
                

me = Alumno('Franco', 'Caputo', "3") 

me.introduction()
me.add_notes("matematica",3)
me.add_notes("matematica",6)
me.add_notes("programacion", 9)
me.add_notes("programacion", 4)
me.show_promedy()