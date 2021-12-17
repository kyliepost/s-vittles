# Vittles
Vittles allows users to bring their family recipes to the internet for those in their family to view and add to.  Instead of digging through old scrapbooks in the attic or forgetting where you last left your recipe book, you can now go online to view them!  

# Setup
1. Clone this repository and change to the directory in the terminal.
2. Run pipenv shell
3. Run pipenv install
4. Run migrations and make migrations
5. Seed database with python3 manage.py loaddata {table name} ###LoadData Order 1.users 2.tokens 3.family 4.recipe 5.tag 6.familyBook 7.recipeTag
 Now that your database is set up all you have to do is run the command:
  `python3 manage.py runserver`

# ERD
https://dbdiagram.io/d/61a686ea8c901501c0da213b

# Wireframe
https://sketchboard.me/dashboard/tm_Cr2rsCeI#/


