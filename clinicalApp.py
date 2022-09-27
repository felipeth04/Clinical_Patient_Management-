import os 

os.system('clear')
print("")
print("┌─────────────────────────────────────────────────────────────────┐")
print("│ 🏥 Bienvenidos al sistema de historias clínicas del hospital 🏥 │")
print("└─────────────────────────────────────────────────────────────────┘")
print("")
print("")

def show_menu():
    print("\n ******************************* \n")
    print("🛑  1 - Cargar paciente")
    print("🛑  2 - Buscar paciente")
    print("🛑  3 - Listar pacientes")
    print("🛑  4 - Salir\n")
    print("******************************* \n")
    user_option = input("DEBES INGRESAR UN NUMERO ENTRE 1 Y 4, INTENTA DE NUEVO POR FAVOR. ")
    return user_option

def user_option_validation(response):
    validated = False
    res_number = 0
    message = ""

    if response.isdigit():

        res_number = int(response)
        if(res_number >= 1 and res_number <= 4):
            message = "ESTA EN RANGO "
            validated = True
        else:
            message = "FUERA DE RANGO "
    else:
        message = "ENTRADA INCORRECTA "
    
    return validated, res_number, message

program_running = True
database = list()

while program_running:
    response = show_menu()
    validated, res_number, message = user_option_validation(response)
    
    if validated == True:

        if res_number == 1:
            name = input("INGRESA EL NOMBRE DEL PACIENTE: ")
            age = input("INGRESE LA EDAD DEL PACIENTE: ")
            medical_record = input("INGRESE EL MOTIVO DE CONSULTA: ")
            
            patient = {"name": name, "age": age, "medical_record": medical_record }
            database.append(patient)
            
        elif res_number == 2:

            search_name = input("\nINGRESE EL NOMBRE DEL PACIENTE A CONSULTAR: ")
            patient_finded = True

            for x in range(len(database)):
                if database[x]["name"].lower() == search_name.lower():
                    print("\n┌──────────────────────────────────────┐")
                    print("│   BUSQUEDA EXITOSA DEL PACIENTE      │")
                    print("└──────────────────────────────────────┘\n")
                    print("NOMBRE COMPLETO DEL PACIENTE: ",database[x]["name"].upper())
                    print("EDAD ACTUAL DEL PACIENTE: ", database[x]["age"])
                    print("HISTORIAL CLINICA COMPLETA: ", database[x]["medical_record"])
                else:
                    patient_finded = False

        elif res_number == 3:
            print("\n┌─────────────────────────────┐")
            print("│   LISTADO DE PACIENTES      │")
            print("└─────────────────────────────┘\n")
            for x in range(len(database)):
                print("\n┌─────────────────────────────────────────────────────────────┐")
                print("| NUMERO DE PACIENTE:", "| NOMBRE", "| ULTIMA HISTORIA CLINICA")
                print()
                print("\t",x+1,"\t\t",database[x]["name"].upper(),"\t\t", database[x]["medical_record"])
                print("└─────────────────────────────────────────────────────────────┘\n")
        elif res_number == 4:
            program_running = False
        else:
            print(message)

    else:
        print("")
