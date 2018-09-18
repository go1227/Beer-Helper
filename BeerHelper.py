import random

#Read TXT file and print results that match 'results' array
beer_catalogue = []
file = open("beer_catalogue.txt", "r")
for line in file:
    beer_catalogue.append(line)
file.close()


#Questions
questions = [
    "Question 1/4 - Select your beer type preferences:\n(1) Ale\n(2) Lager\n(3) Stout & Porter\n(4) Malt\n(5) Any type\n\n",
    "Question 2/4 - Beer Origin preferences:\n(1) American\n(2) German\n(3) Mexican\n(4) English\n(5) Japanese\n(6) Netherlands\n(7) Any origin\n\n",
    "Question 3/4 - Select your favorite beer style\n(1) Amber\n(2) Blonde\n(3) Brown\n(4) Cream\n(5) Dark\n(6) Fruit\n(7) Golden\n(8) Honey\n(9) India Pale Pale\n(10) Light\n(11) Lime\n(12) Pale\n(13) Pilsner\n(14) Strong\n(15) Any style\n\n",
    "Question 4/4 - Select the Calories in your Beer\n(1) Low Calories\n(2) Regular\n(3) High calories\n(4) I don't care\n\n"
]

valid_answers = ["1, 2, 3, 4, 5",
                 "1, 2, 3, 4, 5, 6, 7",
                 "1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15",
                 "1, 2, 3, 4"]

q_and_a_dict0 = { 1:"ale", 2:"lager", 3:"stoutandporter", 4:"malt", 5:"any" }
q_and_a_dict1 = { 1:"american", 2:"germany", 3:"mexican", 4:"english", 5:"japanese", 6:"belgium", 7:"any" }
q_and_a_dict2 = { 1:"amber", 2:"blonde", 3:"brown", 4:"cream", 5:"dark", 6:"fruit", 7:"golden", 8:"honey", 9:"indiapaleale", 10:"light", 11:"lime", 12:"pale", 13:"pilsner", 14:"strong", 15:"any" }
q_and_a_dict3 = { 1:"low", 2:"regular", 3:"high", 4:"any" }

answers = []

for question in range(len(questions)):
    possible_answers = ""
    current_answer = input(questions[question])
    possible_answers = valid_answers[question]

    while possible_answers.find(current_answer) == -1:
        print("\n\n ----- Invalid answer! ----- \n----- Please try again -----\n")
        current_answer = input(questions[question])

    tmp_dict = eval("q_and_a_dict"+str(question))
    answers.append(tmp_dict[int(current_answer)])


#beer_info will hold values that will help to build the final beer score - the top socre will be the selected beer
beer_info = [
    ["ale", "budweiser|corona|fruh|lagunitasipa|michelultra|montauk|sierranevada"],
    ["lager",
     "amstel|amstellight|budlight|budlightlime|brooklynlager|coronalight|hefeweizen|heineken|heinekenlight|samadams|saporo|wychwood"],
    ["stoutandporter", "buxton"],
    ["malt", "echigo"],
    ["american",
     "budlight|budlightlime|brooklynlager|budweiser|lagunitasipa|michelultra|montauk|samadams|sierranevada"],
    ["germany", "fruh|hefeweizen"],
    ["mexican", "corona|coronalight"],
    ["english", "buxton|wychwood"],
    ["japanese", "echigo|saporo"],
    ["dutch", "amstel|amstellight|heineken|heinekenlight"],
    ["amber", "brooklynlager|hefeweizen|sierranevada"],
    ["blonde", "amstel|amstellight|budweiser|corona|fruh|montauk|samadams"],
    ["brown", "buxton"],
    ["cream", "buxton|samadams"],
    ["dark", "buxton|wychwood"],
    ["fruit", "budlightlime"],
    ["golden", "amstel|budweiser"],
    ["honey", "echigo"],
    ["indiapaleale", "brooklynlager|lagunitasipa"],
    ["light", "amstellight|budlight|budlightlime|coronalight"],
    ["lime", "budlightlime"],
    ["pale", "amstel|amstellight|heineken|heinekenlight"],
    ["pilsner", "amstel|budweiser|corona|fruh|michelultra|montauk"],
    ["strong", "brooklynlager|buxton|hefeweizen|lagunitasipa|wychwood"],
    ["low", "amstellight|budlight|budlightlime|coronalight|heinekenlight|michelultra"],
    ["regular", "amstel|budweiser|buxton|corona|echigo|fruh|heineken|samadams"],
    ["high", "brooklynlager|hefeweizen|lagunitasipa|montauk|saporo|sierranevada|wychwood"]
]

#Instead of creating the entire "score" table manually, this function does the job
def define_score_table():
    score = []
    tmp = set()
    for i in range(len(beer_info)):
        tmp_values = beer_info[i][1].split("|")
        for v in tmp_values:
            tmp.add(v)
    for names in tmp:
        score.append([names, 0])
    return score


#In every possible match, add points to the correspondent value
def add_points(beer_name):
    #if the selection was "any", add points to all elements in the score list
    if (beer_name == "any"):
        '''for i in range(len(score)):
            score[i][1] += 1'''
    else:
        #find the beer results in Beer_Info
        beer_list = []
        for i in range(len(beer_info)):
            if beer_info[i][0] == beer_name:
                beer_list = beer_info[i][1].split("|")
                break

        for j in range(len(beer_list)):
            for i in range(len(score)):
                if (score[i][0] == beer_list[j]):
                    score[i][1] += 1

#Function used to sort the array and returning the MAX point obtained
def get_max_point(final_score):
    result_set = set()
    for i in range(len(final_score)):
        result_set.add(final_score[i][1])
    max_value = max(result_set)
    return max_value


## PROGRAM EXECUTION ##

#define Score Table
score = define_score_table()

#Add points to Score Table for all beer matches found
for i in range(len(answers)):
    print(answers[i])
    add_points(answers[i])

#Find beer(s) that got the max point: best candidate
max_point = get_max_point(score)
results = []
for i in range(len(score)):
    if (score[i][1] == max_point and max_point != 0):
        results.append(score[i][0])

print(score)

standard_missing_info = "This information is not available at this time"

#For each result, print info from beer_catalogue[] array
if len(results) > 0:
    print("-------------------------------------\nFinal Results:\n-------------------------------------\n")
    for x in range(len(results)):
        for y in range(len(beer_catalogue)):
            #print(results[x] + " == " + beer_catalogue[y].split("|")[0])
            if results[x] == beer_catalogue[y].split("|")[0]:
                print("Suggestion " + str(x+1) + " of " + str(len(results)) + ":\n")

                name = ""
                country = ""
                alcohol = ""
                calories = ""
                beertype = ""

                if (beer_catalogue[y].split("|")[1]):
                    name = beer_catalogue[y].split("|")[1]
                else:
                    name = standard_missing_info

                if (beer_catalogue[y].split("|")[2]):
                    country = beer_catalogue[y].split("|")[2]
                else:
                    country = standard_missing_info

                if (beer_catalogue[y].split("|")[3]):
                    alcohol = beer_catalogue[y].split("|")[3]
                else:
                    alcohol = standard_missing_info

                if (beer_catalogue[y].split("|")[4]):
                    calories = beer_catalogue[y].split("|")[4]
                else:
                    calories = standard_missing_info

                if (beer_catalogue[y].split("|")[5]):
                    beertype = beer_catalogue[y].split("|")[5]
                else:
                    beertype = standard_missing_info

                print("- Name: " + name)
                print("- Country of origin: " + country)
                print("- Alcohol %: " + alcohol)
                print("- Calorie info: " + calories)
                print("- Type: " + beertype)

else:
    print("Unfortunately we couldn't find the perfect beer match for you.\nHowever, we randomly selected a beer that you might like.\nEnjoy it!\n")
    y = random.randint(1,len(beer_catalogue))

    name = ""
    country = ""
    alcohol = ""
    calories = ""
    beertype = ""

    if (beer_catalogue[y].split("|")[1]):
        name = beer_catalogue[y].split("|")[1]
    else:
        name = standard_missing_info

    if (beer_catalogue[y].split("|")[2]):
        country = beer_catalogue[y].split("|")[2]
    else:
        country = standard_missing_info

    if (beer_catalogue[y].split("|")[3]):
        alcohol = beer_catalogue[y].split("|")[3]
    else:
        alcohol = standard_missing_info

    if (beer_catalogue[y].split("|")[4]):
        calories = beer_catalogue[y].split("|")[4]
    else:
        calories = standard_missing_info

    if (beer_catalogue[y].split("|")[5]):
        beertype = beer_catalogue[y].split("|")[5]
    else:
        beertype = standard_missing_info

    print("- Name: " + name)
    print("- Country of origin: " + country)
    print("- Alcohol %: " + alcohol)
    print("- Calorie info: " + calories)
    print("- Type: " + beertype)