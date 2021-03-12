input_data = []
labels = {
    "sw": 0,
    "se": 1,
    "nw": 2,
    "ne": 3,
    "f": 0,
    "m": 1,
    "y": 1,
    "n": 0
}

weights = [-12876.16559496488, 257.2872001114463, -131.12010294992865,
           332.56555407325794, 479.365835078233, 23820.426517426917,
           353.629009425292]


def prompt_number(prompt):
    while(True):
        try:
            input_data.append(abs(float(input(prompt))))
            break
        except ValueError:
            print("Please enter a number")


def prompt_input(prompt, error):
    while(True):
        try:
            input_data.append(labels[input(prompt).lower()])
            break
        except KeyError:
            print(error)


# age
prompt_number("Enter your age: ")

# sex
prompt_input("Are you male or female (m\\f): ", "please input \"m\" if you " +
             "are a male, and \"f\" if you are a female")

# bmi
prompt_number("Enter your BMI (Body Mass Index): ")

# children
prompt_number("How many children?: ")
input_data[3] = int(input_data[3])

# smoker
prompt_input("Are you a smoker? (y\\n): ", "please input \"y\" if you are a " +
             "smoker, and \"n\" if you are not")

# region
prompt_input("Enter your region in the U.S. Southwest\\Southeast\\Northwest" +
             "\\Northeast (sw\\se\\nw\\ne): ", "please input either sw, se, " +
             "nw or ne for your region")

prediction = weights[0]
for entry in range(len(input_data)):
    prediction += input_data[entry]*weights[entry+1]
prediction = abs(prediction)
if prediction < 1500:
    prediction += 1000

print("Your estimated health costs: ${:.2f}".format(prediction))

input()
