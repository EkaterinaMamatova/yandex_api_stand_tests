import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400


def get_new_user_token(user_response):
    return "Bearer " + user_response.json().get("authToken")

data.headers_kit["Authorization"] = get_new_user_token(sender_stand_request.user_response)

#добавила после ревью - негативная проверка для Тест 10. Параметр не передан в запросе

def negative_assert_parameter_not_passed_in_name(name):
    response = sender_stand_request.post_new_client_kit(name)

    assert response.status_code == 400


#Тест 1. Допустимое количество символов (1)

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#Тест 2. Допустимое количество символов (511)

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Тест 3. Количество символов меньше допустимого (0)

def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")

#Тест 4. Количество символов больше допустимого (512)

def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Тест 5. Разрешены английские буквы

def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

#Тест 6. Разрешены русские буквы

def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

#Тест 7. Разрешены спецсимволы

def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert('"№%@",')

#Тест 8. Разрешены пробелы

def test_create_kit_spaces_in_name_get_success_response():
    positive_assert("Человек и КО")

#Тест 9. Разрешены цифры

def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

#Тест 10. Параметр не передан в запросе

def test_create_kit_parameter_not_passed_in_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_parameter_not_passed_in_name(kit_body)

#Тест 11. Передан другой тип параметра (число)

def test_create_kit_other_parameter_type_in_name_get_error_response():
    negative_assert_code_400(123)