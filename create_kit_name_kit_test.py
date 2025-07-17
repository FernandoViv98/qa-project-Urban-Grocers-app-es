#import configuration
import data
import sender_stand_request
import TEST_2_511
import TEST_4_512

def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # Comprueba si el usuario o usuaria existe y es único/a
    print(user_response.status_code)
    print(user_response.json())

def test_positive_new_user():
    positive_assert("Fernando")

#TEST 1 Kit con 1 caracteres (Resultado 201)
def test_create_kit_1_letter_in_kit_body():
    response = sender_stand_request.create_new_kit({"name": "a"})
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

#TEST 2 Kit con 511 caracteres (Resultado 201)
def test_create_kit_511_letter_in_kit_body():
    response = sender_stand_request.create_new_kit(TEST_2_511.value511)
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

#TEST 3 Kit con 0 caracteres, (Debe de dar 400 pero da 201)
def test_create_kit_0_letter_in_kit_body():
    response = sender_stand_request.create_new_kit({ "name": "" })
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

#TEST 4 Kit con 512 caracteres (Debe de dar 400 pero da 201)
def test_create_kit_512_letter_in_kit_body():
    response = sender_stand_request.create_new_kit(TEST_4_512.value512)
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

#TEST 5 Kit con caracteres especiales (Resultado 201)
def test_create_kit_special_letter_in_kit_body():
    response = sender_stand_request.create_new_kit({"name": "№%@,"})
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())