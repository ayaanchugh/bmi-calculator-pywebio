from asyncio import start_server
from pywebio.input import input, FLOAT
from pywebio.output import put_text

def calculate_bmi():
   height = input("Enter your height (in cm)", type=FLOAT)
   weight = input("Enter your weight (in kg)", type=FLOAT)
   bmi = weight / ((height/100) ** 2)
   bmi = round(bmi, 2)
   weight_category = ""
   if bmi < 18.5:
      weight_category = "underweight"
   elif 18.5 <= bmi <= 24.9:
      weight_category = "normal weight"
   elif 25 <= bmi <= 29.9:
      weight_category = "overweight"
   else:
      weight_category = "obese"
   put_text("Your BMI is: %s" % bmi)
   put_text("You have a %s" % weight_category)


if __name__ == '__main__':
    calculate_bmi()
   
# # A simple script to calculate BMI
# from pywebio.input import input, FLOAT
# from pywebio.output import put_text

# def bmi():
#     height = input("Input your height(cm)：", type=FLOAT)
#     weight = input("Input your weight(kg)：", type=FLOAT)

#     BMI = weight / (height / 100) ** 2

#     top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
#                   (25, 'Normal'), (30, 'Overweight'),
#                   (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

#     for top, status in top_status:
#         if BMI <= top:
#             put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
#             break

# if __name__ == '__main__':
#     bmi()