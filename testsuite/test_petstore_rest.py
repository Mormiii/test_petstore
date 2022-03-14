import pytest
from pytest_bdd import given,when,then,scenario, parsers
import requests as REST
import json
from json import JSONDecodeError




Body ={
  "id": "",
  "name": "",
  "status": "available"

}
header = {"accept": "application/json"}

url_api_pet ='https://petstore.swagger.io/v2/pet'

#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/petstore_rest.feature","Add new pet to the store")
def test_create_pet():
    pass

#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/petstore_rest.feature","Find pet by ID")
def test_find_pet():
    pass


#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/petstore_rest.feature","Delete a pet")
def test_delete_pet():
    pass


@given(parsers.parse("request body with {petname}, {id}"),target_fixture="Body")
def fill_request_body(petname,id):
    if id =='empty':
        Body['id']=''
    else:
        Body["name"]= petname
        Body["id"]= id
    #print(Body)
    return Body

@given("petstore with pets created")
def petstore_not_empty():
    pass


@when(parsers.parse("POST request arrives to endpoint"), target_fixture="response")
def post_request(Body):
    header['Content-Type']='application/json'
    print(f"Sending POST request to endpoint: {url_api_pet}, with Body: {json.dumps(Body)} and header: {header}")
    response = REST.post(url_api_pet, data =json.dumps(Body, indent=2), headers =header)
    print(f"The response is: {response.text}")
    try:
        return response
    except JSONDecodeError:
        print("The response can't be converted to JSON")


#    resp = REST.put(url_create_space_filled, data = json.dumps(body, indent =2) , headers=headers)


@when(parsers.parse("GET request arrives to endpoint/{id}"), target_fixture="response")
def get_request(id):

    url_api_pet_with_id = url_api_pet+f'/{id}'
    print(f"Sending GET request to endpoint: {url_api_pet_with_id}")
    response = REST.get(url_api_pet_with_id, headers = header)
    print(f"The response is: {response.text}")
    print(response.status_code)
    try:
        #resp= response.json()
        return response
    except JSONDecodeError:
        print("The response can't be converted to JSON")


@when(parsers.parse("DELETE request arrives to endpoint/{id}"), target_fixture="response")
def delete_request(id):
    url_api_pet_with_id = url_api_pet+f'/{id}'
    print(f"Sending DELETE request to endpoint: {url_api_pet_with_id}")
    response = REST.delete(url_api_pet_with_id, headers= header)
    print(f"The response is: {response.text}")
    print(response.status_code)
    try:
        #resp= response.json()
        return response
    except JSONDecodeError:
        print("The response can't be converted to JSON")




@then(parsers.parse("{response_statuscode} is responded"))
def check_response(response, response_statuscode):
    print("resp", response)
    #print(f"Response.json is: {resp}")
    #print(f"The response code is:{resp['code']},| and the expected status is:",response_statuscode)
    assert int(response_statuscode) == int(response.status_code)




