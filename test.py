import json

import requests


def test_add_new_pet():  # POST/pet Add a new Pet to the store
    input_pet = {
        "id": 45,
        "category": {
            "id": 32,
            "name": "Nino"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 10,
                "name": "Okley"
            }
        ],
        "status": 'available'
    }
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    print("POST/pet Add a new Pet to the store")
    print('Cтатус запроса:', res_post.status_code)
    res_json = json.loads(res_post.text)
    assert input_pet == res_json
    print('Ответ сервера body:', res_post.json())


def test_update_pet():  # PUT/pet Update an existing pet
    input_pet = {
        "id": 45,
        "category": {
            "id": 32,
            "name": "Crazy"
        },
        "name": "cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 10,
                "name": "Okley"
            }
        ],
        "status": 'available'
    }
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res_put = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    print("PUT/pet Update an existing pet")
    print('Cтатус запроса:', res_put.status_code)
    res_json = json.loads(res_put.text)
    assert input_pet == res_json
    print('Ответ сервера body:', res_put.json())


def test_pet_id():  # GET/pet {petId} find pet dy ID
    input_pet = {
        "id": 45,
        "category": {
            "id": 32,
            "name": "Crazy"
        },
        "name": "cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 10,
                "name": "Okley"
            }
        ],
        "status": 'available'
    }

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
    assert res_get.status_code == 200
    assert json.loads(res_get.text) == input_pet
    print("GET/pet {petId} find pet dy ID")
    print('Cтатус запроса:', res_get.status_code)
    print('Ответ сервера body:', res_get.json())


def test_del_pet():  # DELETE/pet {petId} Deletes a pet
    input_pet = {
        "id": 45,
        "category": {
            "id": 32,
            "name": "Crazy"
        },
        "name": "cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 10,
                "name": "Okley"
            }
        ],
        "status": 'available'
    }
    res_del = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
    out_del = {
  "code": 200,
  "type": "unknown",
  "message": "45"
}
    assert json.loads(res_del.text) == out_del
    assert json.loads(res_del.text) == out_del
    print("DELETE/pet {petId} Deletes a pet")
    print('Cтатус запроса:', res_del.status_code)
    print('Ответ сервера body:', res_del.json())
