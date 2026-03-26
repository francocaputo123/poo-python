class Usuario:
    def __init__ (self,name, surname, rol) :
        self.name = name
        self.surname = surname
        self.rol = rol
        

    def get_fullname(self) :
        return (self.name, self.surname)

    def get_name(self) :
        return self.name

    def set_name(self,name) :
        self.name = name


class Usuarios:
    def __init__(self,user_list) :
        self.user_list = user_list

    def add_user(self, Usuario) :
        self.user_list.append(Usuario) 

    def show_users(self) :
        i = 0
        while i < len(self.user_list) :
            print(self.user_list[i].get_fullname())
            i += 1

    def remove_user_by_name(self,name) : 
        if len(self.user_list) == 0 :
            return print('No hay usuarios')

        i = 0
        if i < len(self.user_list) :
            if self.user_list[i].get_name() == name :
                self.user_list.pop(i)
            i += 1


yo = Usuario('franco', 'caputo', 'estudiante')
ez = Usuario('ezequiel', 'monzon', 'estudiante')
elmascapito = Usuario('enzo', 'silva', 'estudiante')
usuarios = []
lista = Usuarios(usuarios)
lista.add_user(yo)
lista.add_user(ez)
lista.add_user(elmascapito)
lista.show_users()
lista.remove_user_by_name('franco') 
print("--------------------------------------------")
lista.show_users()