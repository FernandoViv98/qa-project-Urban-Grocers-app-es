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

def positive_assert_kit(name_kit):
    kit_body = {"name": name_kit}
    response = sender_stand_request.create_new_kit(kit_body)

    assert response.status_code == 201
    assert response.json()["authToken"] != ""
    assert response.json()["name"] == name_kit
    print("Prueba positiva para parametro:", {name_kit})
    print(response.status_code)
    print(response.json())

def negative_assert_kit(name_kit):
    kit_body = {"name": name_kit}
    response = sender_stand_request.create_new_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"
    print(response.status_code)
    print(response.json())

#TEST 1 Kit con 1 caracteres (Resultado 400 Esperado 201)
def test_create_kit_1_letter_in_kit_body():
    positive_assert_kit("a")

#TEST 2 Kit con 511 caracteres (Resultado 400 Esperado 201)
def test_create_kit_511_letter_in_kit_body():
    positive_assert_kit(TEST_2_511.value511)

#TEST 3 Kit con 0 caracteres, (Resultado 400 Esperado 400)
def test_create_kit_0_letter_in_kit_body():
    negative_assert_kit("")

#TEST 4 Kit con 512 caracteres (Resultado 400 Esperado 400)
def test_create_kit_512_letter_in_kit_body():
    negative_assert_kit(TEST_4_512.value512)

#TEST 5 Kit con caracteres especiales (Resultado 400 Esperado 201)
def test_create_kit_special_letter_in_kit_body():
    positive_assert_kit("№%@,")

#TEST 6 Kit con espacios (Resultado 400 Esperado 201)
def test_create_kit_space_in_kit_body():
    positive_assert_kit("A Aaa")

#TEST 7 Kit con numeros en el nombre (Resultado 400 Esperado 201)
def test_create_kit_numbers_in_kit_body():
    positive_assert_kit("123")

#TEST 8 Kit sin parametro en solicitud "kit_body = { }" (Resultado 400 Esperado 400)
def test_create_kit_no_json_kit_body():
    negative_assert_kit(None)

#TEST 9 Kit con parametro diferente "kit_body = {"name": 123}" (Resultado 400 Esperado 400)
def test_create_kit_dif_param_kit_body():
    negative_assert_kit(123)