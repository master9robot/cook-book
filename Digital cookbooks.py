
while True:

   user_action = input("Hi i'm chef, your digital cookbook what would you like to make(cheesy pasta, lassana, bacon pancakes): ")
   if "cheesy pasta" in user_action:
      print('''CHEESY PASTA
Ingreidients:
any kind of pasta, parmesan, ricotta, shredded mozzarella, chicken, onions, garlic, and a combo of tomato sauce, tomato paste, and crushed tomatoes

1.Boil your pasta while you prep the other ingredients

2.Cut up your veggies and blend half of them before adding them to a wok like pan to cook

3.Cook and season your chicken then add it to the sauce

4.Once pasta is boiled add the sauce and then mix in the pasta

5.Now enjoy your wonderful food

''')
   elif "lassana" in user_action:
      print('''LASSANA
Ingreidients:
lassana noodles, parmesan, ricotta, shredded mozzarella, ground beef, bacon, onions, garlic, and a combo of tomato sauce, tomato paste, and crushed tomatoes

1.Start by making the sauce with ground beef, bacon, onions, garlic, and a combo of tomato sauce, tomato paste, and crushed tomatoes. The three kinds of tomatoes gives the sauce great depth of flavor.

2.Get the cheeses ready. We're using ricotta, shredded mozzarella, and parmesan -- like the mix of tomatoes, this 3-cheese blend gives the lasagna great flavor!

3.From there, it's just an assembly job. A cup of meat sauce, a layer of lassana noodles, more sauce, followed by a layer of cheese. Repeat until you have three layers and have used up all the ingredients.

4.Bake for 30 - 40 minutes and you're ready to eat!
''')
   elif "bacon pancakes" in user_action:
      print('''BACON PANCAKES
Ingreideints:
bacon, plain flour, 2 large eggs, milk, sunflower or vegetable oil and a pinch of salt 

Put plain flour, 2 large eggs, milk, sunflower or vegetable oil and a pinch of salt into a bowl or large jug, then whisk to a smooth batter, this should be similar in consistency to single cream.

Set aside for 30 mins to rest

Cook your bacon until almost crispy

Then dip your bacon in the batter , making sure to cover it , and fry it like normal till the pancake is golden brown
            ''')
   else :
      print("please pic a recipe")

   retry = input("New recipe? (y/n): ")
   if retry.lower() != "y": 
    break

