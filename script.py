import numpy as np

#Save cupcakes recipe as an array
cupcakes = np.array([2, 0.75, 2, 1 , 0.5])

#Load recipes file
recipes = np.genfromtxt("recipes.csv", delimiter=",")
print(recipes)

#Show eggs only
eggs = recipes[:,2]

#Recipes with exactly one egg
one_egg = recipes[(eggs==1)]

#Create cookies recipe
cookies = recipes[2,:]

#Create double batch of cookies 
double_batch = cupcakes * 2

#Create grocery list
grocery_list = cookies + double_batch