
import time
from os import system, name
from time import sleep

course_register = {
    1: 'Introduccion a programacion',
    2: 'Fundamentos bases de datos',
    3: 'Programacion orientada a objetos'
}
course_index = 0

def print_initial():
    print ('\n***** PlatziBook ***** \n')
    print ('Elige un commando:')
    print ('[1] Crear un curso')
    print ('[2] Editar un curso')
    print ('[3] Eliminar un curso ')
    print ('[4] Ver cursos registrados')  
    print ('[5] Salir \n')  

def select_action(num):
    
    if num == 1:
        
        new_course= input('Ingresa el nombre del nuevo curso: ')
        create_new_course(new_course)
        print('Curso Agregado')
        print(course_register)
        time.sleep(3)
        clear()
        run()
        

    elif num == 2:
        if course_register != {}:
            
            print (course_register)
            course_index = int(input('Selecciona numero de curso a editar: '))
            name_edition = input('Ingresa nuevo nombre del curso: ')
            edit_course(course_index,name_edition)
            print('Nombre editado')
            print(course_register)
            time.sleep(3)
            clear()
            run()
            
        else:
            print('No hay cursos registrados')
            run()
    elif num == 3:
        if course_register != {}:
            print (course_register)
            course_index = int(input('Selecciona numero de curso a eliminar: '))
            remove_course(course_index)
            
        else:
            print('No hay cursos registrados')
            run()

    elif num == 4:
        if course_register != {}:
            print (course_register)
            time.sleep(5)
            run()
        else:
            print('No hay cursos registrados')
            run()
    elif num == 5:
        exit
    else:
        print('Comando invalido. Ingrese numero de 1 a 5')
        time.sleep(1)
        run()

def create_new_course(new):
    max_index = len(course_register) + 1
    course_register[max_index]= new
    
def edit_course(key, name):
    if 0 < key <= len(course_register):
        course_register[key] = name
    else:
        print('El curso no existe')
        run()

def remove_course(key):
    if 0 < key <= len(course_register):
        for i in course_register:
            if i >= key and i < len(course_register):
                course_register[i]=course_register[i+1]
        course_register.pop(len(course_register))
        print('Curso eliminado ')
        print(course_register)
        time.sleep(3)
        clear()
        run()
    else:
        print('El curso no existe')

def clear():
    
        #for windows
        if name == 'nt':
            _ = system('cls')
        
        #for mac and linux
        else:
            _ = system('clear')


def run():
    
    print_initial()
    command = int(input('Ingresa un numero de comando:'))
    select_action(command)  


if __name__ == '__main__':
    run()