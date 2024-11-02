# M02 IF THEN ELSE statements Book 4.2
# Author: Carey Armstrong
# Date: 2024-11-02
# Revision: 1.0

# Set up dictionary with values
veggiedict = {"cherry": ["red", "small"], "pea": ["green", "small"], "watermelon": ["green", "large"],
              "pumpkin": ["orange", "large"]}

# For loop with embedded if / else statements
for key, value in veggiedict.items():
    if value == ["green", "small"]:
        green_small = True
        if green_small == True:
            print("This veggie meets the parameters green & small: ", key)
    else:
        not_green_small = False
        if not_green_small == False:
            print("These veggies do not meet the parameters green & small: ", key)
