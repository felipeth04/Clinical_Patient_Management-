print("\n *****************************************************************************")
print("WELCOME TO CLINIC APP, THE BEST APPLICATION FOR THE MANAGEMENT OF YOUR PATIENTS")
print("********************************************************************************")

def show_menu():
    print("\n ******************************* \n")
    print("1.   Crear paciente:   ")
    print("2.   Buscar paciente por nombre: ")
    print("3.   Listar usuarios: ")
    print("4.   Salir del programa: \n")
    print("******************************* \n")
    user_option = input("Selecciona una opción del 1 al 4 por favor: ")
    return user_option

def user_option_validation(response):
    validated = False
    res_number = 0
    message = ""

    if response.isdigit():

        res_number = int(response)
        if(res_number >= 1 and res_number <= 4):
            message = "Esta en rango"
            validated = True
        else:
            message = "fuera de rango"
    else:
        message = "Entrada incorrecta"
    
    return validated, res_number, message

program_running = True
database = list()

while program_running:
    response = show_menu()
    validated, res_number, message = user_option_validation(response)
    
    if validated == True:

        if res_number == 1:
            name = input("Ingrese su nombre por favor: ")
            age = input("Ingrese su edad por favor: ")
            medical_record = input("Ingrese su motivo de consulta por favor: ")
            
            patient = {"name": name, "age": age, "medical_record": medical_record }
            database.append(patient)
            

        elif res_number == 2:

            search_name = input("Ingrese el nombre del paciente por favor: ")
            name.lower()

            for x in range(len(database)):
                for key, value in database[x].items():
                    if key == name and value == search_name:
                        print(database[x]["name"].upper())
                        print("Successful patient search | Medical Record:", database[x]["medical_record"])
                    else:
                        print("paciente no encontrado")


        elif res_number == 3:
            print("")
        elif res_number == 4:
            print("")
        else:
            print("")

    else:
        print("")
