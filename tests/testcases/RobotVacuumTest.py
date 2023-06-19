import pytest
import requests
import json
import assertpy


from pytest_bdd import scenario, given, when, then

global input_dict, api_url, json_content, patches_num, count_patches, new_cleared_patches
room_size = [0, 0]
point_coords = [0, 0]
new_cleared_patches = []
api_url = "http://localhost:8080/v1/cleaning-sessions"
json_content = '{ "roomSize" : [5, 5], "coords" : [1, 2], "patches" : [ [1, 0], [2, 3], [2, 2] ], "instructions" : "NNESEESWNWW" }'


@scenario('Example.feature', 'Robot Vacuum service execution')
def test_1():
    pass

@given('API end point is given')
def service_url():
    global api_url
    api_url = "http://localhost:8080/v1/cleaning-sessions"

@when('JSON input is provided')
def json_input():
    global json_content,  input_dict
    json_content = '{ "roomSize" : [5, 5], "coords" : [1, 2], "patches" : [ [1, 0], [2, 2], [2, 3],[1,4] ], "instructions" : "NNESEESWNWW" }'
    input_dict = json.loads(json_content)

    print(input_dict)


@pytest.fixture
def imp_value():
    pass

@when('API is called')
def api_call():
    global api_output, response
    response = requests.post(api_url, json=json.loads(json_content))
    response.json()


@then('Service returns Success status 200')
def api_response():
    # if response.status_code == 200:
    #     print("Success")
    # else:
    #     print("Fail")

    assert response.status_code == 200, print("Success response")


@scenario('Example.feature', 'Navigation coordinates traversal')
def test_2():
    pass


input_dict = json.loads(json_content)
point_coords = input_dict['coords']
room_size = input_dict['roomSize']


@given('Starting co-ords')
def init_coords():
    # global point_coords
    #point_coords = input_dict['coords']
    print("Point")
    print(point_coords[1] + 1)


@given('Room size')
def room_size2():
    # global room_size
    print("Room size")
    print(input_dict['roomSize'])
    #room_size = input_dict['roomSize']
    print("After")
    print(room_size)


@given('Direction instruction string (N/S/E/W)')
def init_directions():
    global nav_instruction
    nav_instruction = input_dict['instructions']


@when('API is called 2')
def api_call_1():
    global api_output, response_1
    response_1 = requests.post(api_url, json=input_dict)
    api_output = response_1.json()
    print("hello")
    print(api_output)


@pytest.fixture
def imp_value_1():
    pass


@then('Ending coordinates are calculated correctly')
def navigation():
    for i in nav_instruction:
        print(i)
        # if point_coords[0] < room_size[0] or point_coords[1] < room_size[1] :
        if i == "N":
            is_north()
        elif i == "S":
            is_south()
        elif i == "E":
            is_east()
        elif i == "W":
            is_west()

        print('point_coords')
        print(point_coords)

        #/Trial
        temp = [point_coords[0], point_coords[1]]
        if point_coords in input_dict['patches'] and temp not in new_cleared_patches:
            # if point_coords not in new_cleared_patches:
            #if new_cleared_patches.index(point_coords):
            new_cleared_patches.append(temp)
            print("Added")
            print(temp)
            print("Cleared")
            print(point_coords)

        print(len(new_cleared_patches))

    if (point_coords != api_output):
        print("Failed navigation")

def is_east():
    if point_coords[1] + 1 < room_size[1]:
        point_coords[1] = point_coords[1] + 1
    # return point_coords


def is_west():
    if point_coords[1] - 1 >= 0:
        point_coords[1] = point_coords[1] - 1
    # return point_coords


def is_north():
    if point_coords[0] + 1 < room_size[0]:
       point_coords[0] = point_coords[0] + 1
    #return point_coords

def is_south():
    if point_coords[0] - 1 >= 0:
        point_coords[0] = point_coords[0] - 1
    # return point_coords

# def patches_cleared(current_patch):
#     patches_num = input_dict['patches']
#
#     if current_patch in patches_num:
#         count_patches = count_patches + 1
#         return count_patches



@scenario('Example.feature', 'Robot Vacuum calibration')
def test_3():
    pass
nav_dir= input_dict['instructions']


@given('Instructions provided in the JSON')
def isValidDirection():
    global cardinal_directions
    cardinal_directions = ["N", "S", "E", "W"]


@then('Verify the directions are valid')
def validDir():
    assert [i in cardinal_directions for i in nav_dir], print("Correct directions")
