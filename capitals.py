import random 
# an array of state dictionaries
# states = [
# {
#     "name": "Alabama",
#     "capital": "Montgomery"
# }, {
#     "name": "Alaska",
#     "capital": "Juneau"
# }, {
#     "name": "Arizona",
#     "capital": "Phoenix"
# }, {
#     "name": "Arkansas",
#     "capital": "Little Rock"
# }, {
#     "name": "California",
#     "capital": "Sacramento"
# }, {
#     "name": "Colorado",
#     "capital": "Denver"
# }, {
#     "name": "Connecticut",
#     "capital": "Hartford"
# }, {
#     "name": "Delaware",
#     "capital": "Dover"
# }, {
#     "name": "Florida",
#     "capital": "Tallahassee"
# }, {
#     "name": "Georgia",
#     "capital": "Atlanta"
# }, {
#     "name": "Hawaii",
#     "capital": "Honolulu"
# }, {
#     "name": "Idaho",
#     "capital": "Boise"
# }, {
#     "name": "Illinois",
#     "capital": "Springfield"
# }, {
#     "name": "Indiana",
#     "capital": "Indianapolis"
# }, {
#     "name": "Iowa",
#     "capital": "Des Moines"
# }, {
#     "name": "Kansas",
#     "capital": "Topeka"
# }, {
#     "name": "Kentucky",
#     "capital": "Frankfort"
# }, {
#     "name": "Louisiana",
#     "capital": "Baton Rouge"
# }, {
#     "name": "Maine",
#     "capital": "Augusta"
# }, {
#     "name": "Maryland",
#     "capital": "Annapolis"
# }, {
#     "name": "Massachusetts",
#     "capital": "Boston"
# }, {
#     "name": "Michigan",
#     "capital": "Lansing"
# }, {
#     "name": "Minnesota",
#     "capital": "St. Paul"
# }, {
#     "name": "Mississippi",
#     "capital": "Jackson"
# }, {
#     "name": "Missouri",
#     "capital": "Jefferson City"
# }, {
#     "name": "Montana",
#     "capital": "Helena"
# }, {
#     "name": "Nebraska",
#     "capital": "Lincoln"
# }, {
#     "name": "Nevada",
#     "capital": "Carson City"
# }, {
#     "name": "New Hampshire",
#     "capital": "Concord"
# }, {
#     "name": "New Jersey",
#     "capital": "Trenton"
# }, {
#     "name": "New Mexico",
#     "capital": "Santa Fe"
# }, {
#     "name": "New York",
#     "capital": "Albany"
# }, {
#     "name": "North Carolina",
#     "capital": "Raleigh"
# }, {
#     "name": "North Dakota",
#     "capital": "Bismarck"
# }, {
#     "name": "Ohio",
#     "capital": "Columbus"
# }, {
#     "name": "Oklahoma",
#     "capital": "Oklahoma City"
# }, {
#     "name": "Oregon",
#     "capital": "Salem"
# }, {
#     "name": "Pennsylvania",
#     "capital": "Harrisburg"
# }, {
#     "name": "Rhode Island",
#     "capital": "Providence"
# }, {
#     "name": "South Carolina",
#     "capital": "Columbia"
# }, {
#     "name": "South Dakota",
#     "capital": "Pierre"
# }, {
#     "name": "Tennessee",
#     "capital": "Nashville"
# }, {
#     "name": "Texas",
#     "capital": "Austin"
# }, {
#     "name": "Utah",
#     "capital": "Salt Lake City"
# }, {
#     "name": "Vermont",
#     "capital": "Montpelier"
# }, {
#     "name": "Virginia",
#     "capital": "Richmond"
# }, {
#     "name": "Washington",
#     "capital": "Olympia"
# }, {
#     "name": "West Virginia",
#     "capital": "Charleston"
# }, {
#     "name": "Wisconsin",
#     "capital": "Madison"
# }, {
#     "name": "Wyoming",
#     "capital": "Cheyenne"
# }]

test_list = [
{
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}]


random.shuffle(test_list)
for state in test_list:
    state.update({'correct':0, 'incorrect':0}) 
def add_points():
    state['correct']+=1 
    print(f"correct! you have {state['correct']} right and {state['incorrect']} wrong")
    if state['correct'] + state['incorrect'] == 3:
        play_again = input(f"You got {state['correct']} correct and {state['incorrect']} wrong. Would you like to play again?")
        state.update({'correct':0, 'incorrect':0}) 
        if play_again == "yes":
            game_start()
        else:
            print("Thank you for playing!")
def sad_points():
    state['incorrect']+=1
    print(f"incorrect! you have {state['correct']} right and {state['incorrect']} wrong")
    if state['correct'] + state['incorrect'] == 3:
        play_again = input(f"You got {state['correct']} correct and {state['incorrect']} wrong. Would you like to play again?")
        if play_again == "yes":
            state.update({'correct':0, 'incorrect':0}) 
            game_start()
        else:
            print("Thank you for playing!")
def game_start():
    random.shuffle(test_list)
    print("Do you know your capitals?")
    for state in test_list:
        capital = input(f"what is the capital of {state['name']}?")
        if capital == f"{state['capital']}":
            add_points()    
        else: 
            sad_points() 
       
 # play_again = input(f"You got {state['correct']} correct and {state['incorrect']} wrong. Would you like to play again?")
        # if play_again == "yes":
        #     game_start()
        # else:
        #     print("Thank you for playing!")        

game_start()

# capital = input(f"what is the capital of {state['name']}?")

# state['correct']= state['correct']+1
# .update()
# for index in test_list:

# if input == test_list


# state_list = []
# for state in test_list:
#     state_list.append(state['name'])



# for state in testList[index].items():
#     print("name")





# capitals = input(f"What is the capital of {state}")
