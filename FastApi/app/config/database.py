"""
Module for defining database models using the Peewee ORM.
"""
from dotenv import load_dotenv
from peewee import (
    AutoField, CharField, ForeignKeyField, IntegerField,
    Model, TextField, MySQLDatabase
)
from config.settings import DATABASE

# Load environment variables from a .env file
load_dotenv()

# MySQL database configuration
database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)

# pylint: disable=too-few-public-methods

class UserModel(Model):
    """Model for representing a user in the system."""
    id = AutoField(primary_key=True)           # Unique identifier for the user
    cc = CharField(max_length=20)              # ID card number
    name = CharField(max_length=50)            # User's name
    lastName = CharField(max_length=50)        # User's last name
    password = CharField(max_length=50)        # User's password
    email = CharField(max_length=50)           # User's email address
    phoneNumber = CharField(max_length=50)     # Phone number
    role = IntegerField()                       # User's role (e.g., 0=user, 1=admin)

    class Meta:
        database = database
        table_name = "user"

class RecipeModel(Model):
    """Model representing a recipe."""
    id = AutoField(primary_key=True)            # Unique identifier for the recipe
    name = CharField(max_length=50)             # Name of the recipe
    typeOfFood = CharField(max_length=50)       # Type of food
    preparationTime = IntegerField()             # Preparation time in minutes
    nutritionalInfoId = IntegerField()          # Nutritional information ID
    images = TextField()                         # Recipe image URLs
    preparationProcess = CharField(max_length=50) # Preparation process

    class Meta:
        database = database
        table_name = "recipe"

class FoodModel(Model):
    """Model representing a food item."""
    id = AutoField(primary_key=True)            # Unique identifier for the food item
    name = CharField(max_length=50)             # Name of the food item
    macronutrientsId = IntegerField()            # Macronutrients ID
    micronutrientsId = IntegerField()            # Micronutrients ID

    class Meta:
        database = database
        table_name = "food"

class IngredientModel(Model):
    """Model representing an ingredient."""
    id = AutoField(primary_key=True)            # Unique identifier for the ingredient
    foodId = ForeignKeyField(FoodModel, backref="food")  # Associated food ID
    quantity = IntegerField()                    # Quantity of the ingredient
    measurementUnit = CharField(max_length=50)   # Measurement unit
    expirationDate = CharField(max_length=50)    # Expiration date
    measure = IntegerField()                     # Measure

    class Meta:
        database = database
        table_name = "ingredient"

class MeasureModel(Model):
    """Model representing measurement units."""
    id = AutoField(primary_key=True)            # Unique identifier for the measure
    name = CharField(max_length=50)             # Name of the measure

    class Meta:
        database = database
        table_name = "measure"

class NotificationModel(Model):
    """Model representing a notification."""
    id = AutoField(primary_key=True)            # Unique identifier for the notification
    userId = ForeignKeyField(UserModel, backref="user")  # Associated user ID
    message = CharField(max_length=50)          # Notification message
    dateSent = CharField(max_length=20)         # Date sent
    type = CharField(max_length=20)              # Type of notification

    class Meta:
        database = database
        table_name = "notification"

class NutritionalInfoModel(Model):
    """Model representing nutritional information."""
    id = AutoField(primary_key=True)            # Unique identifier for the nutritional information
    calories = IntegerField()                    # Calories
    carbohydrates = IntegerField()               # Carbohydrates
    proteins = IntegerField()                    # Proteins
    fats = IntegerField()                        # Fats
    vitamins = CharField(max_length=50)         # Vitamins
    minerals = CharField(max_length=50)         # Minerals

    class Meta:
        database = database
        table_name = "nutritionalInfo"

class PantryModel(Model):
    """Model representing a user's pantry."""
    id = AutoField(primary_key=True)            # Unique identifier for the pantry
    userId = ForeignKeyField(UserModel, backref="user")  # Associated user ID
    ingredientIds = ForeignKeyField(IngredientModel, backref="ingredient")  # Ingredient IDs
    dateLastUpdated = CharField(max_length=50)  # Last updated date

    class Meta:
        database = database
        table_name = "pantry"

class PurchaseHistoryModel(Model):
    """Model representing a user's purchase history."""
    id = AutoField(primary_key=True)            # Unique identifier for the history
    userId = ForeignKeyField(UserModel, backref="user")  # Associated user ID
    ingredientsId = ForeignKeyField(IngredientModel, backref="ingredient")  # Purchased ingredient IDs
    purchaseDate = CharField(max_length=50)     # Purchase date

    class Meta:
        database = database
        table_name = "purchaseHistory"

class RecipeSuggestionModel(Model):
    """Model for recipe suggestions."""
    id = AutoField(primary_key=True)            # Unique identifier for the suggestion
    userId = ForeignKeyField(UserModel, backref="books")  # User ID receiving the suggestion
    suggestedRecipeId = ForeignKeyField(RecipeModel, backref="books")  # Suggested recipe ID
    matchedIngredientId = ForeignKeyField(IngredientModel, backref="ingredient")  # Matched ingredient ID
    missingIngredientesId = ForeignKeyField(IngredientModel, backref="ingredient")  # Missing ingredients IDs
    dateSuggested = CharField(max_length=50)    # Date of the suggestion

    class Meta:
        database = database
        table_name = "recipeSuggestion"

class RolesModel(Model):
    """Model representing user roles."""
    id = AutoField(primary_key=True)            # Unique identifier for the role
    roleName = CharField(max_length=50)         # Role name

    class Meta:
        database = database
        table_name = "roles"

class ShoppingListModel(Model):
    """Model representing a shopping list."""
    id = AutoField(primary_key=True)            # Unique identifier for the list
    userId = ForeignKeyField(UserModel, backref="books")  # Associated user ID
    ingredientId = ForeignKeyField(IngredientModel, backref="books")  # Ingredient ID
    dateCreated = CharField(max_length=20)      # Creation date of the list

    class Meta:
        database = database
        table_name = "shoppingList"

class StoreModel(Model):
    """Model representing a store."""
    id = AutoField(primary_key=True)            # Unique identifier for the store
    name = CharField(max_length=50)             # Store name
    location = CharField(max_length=20)         # Store location
    inventoryId = ForeignKeyField(PantryModel, backref="pantry")  # Associated pantry ID

    class Meta:
        database = database
        table_name = "store"

class UserPreferencesModel(Model):
    """Model representing user preferences."""
    id = AutoField(primary_key=True)            # Unique identifier for the preferences
    userId = ForeignKeyField(UserModel, backref="user")  # Associated user ID
    dietaryRestrictions = CharField(max_length=50)  # Dietary restrictions
    preferredCuisines = CharField(max_length=50)   # Preferred cuisines
    allergens = CharField(max_length=50)           # Allergens

    class Meta:
        database = database
        table_name = "userPreferences"

class WeeklyMenuModel(Model):
    """Model representing a weekly menu."""
    id = AutoField(primary_key=True)            # Unique identifier for the weekly menu

    class Meta:
        database = database
        table_name = "weeklyMenu"

class MenuHistoryModel(Model):
    """Model representing a user's menu history."""
    id = AutoField(primary_key=True)            # Unique identifier for the history
    userId = ForeignKeyField(UserModel, backref="user")  # Associated user ID
    weeklyMenuId = ForeignKeyField(WeeklyMenuModel, backref="weeklyMenu")  # Weekly menu ID
    dateCreated = CharField(max_length=20)      # Creation date of the history

    class Meta:
        database = database
        table_name = "menuHistory"

class MenuModel(Model):
    """Model representing the relationship between menus and recipes."""
    id = AutoField(primary_key=True)
    weeklyMenuId = ForeignKeyField(WeeklyMenuModel, backref="weeklyMenu")
    day = CharField(max_length=10)
    hour = CharField(max_length=20)
    type = CharField(max_length=20)

    class Meta:
        """Class defining properties of the Menu model."""
        database = database
        table_name = "menu"

class FavoriteRecipe(Model):
    """Model representing users' favorite recipes."""
    id = AutoField(primary_key=True)            # Unique identifier for the favorite recipe
    userId = ForeignKeyField(UserModel, backref="recipes")  # User ID marking the recipe as favorite
    recipeId = ForeignKeyField(RecipeModel, backref="recipes")  # Recipe ID marked as favorite

    class Meta:
        database = database
        table_name = "favoriteRecipe"

class RecipeIngredient(Model):
    """Model representing the ingredients of a recipe."""
    recipeId = ForeignKeyField(RecipeModel, backref="ingredient")  # ID of the associated recipe
    ingredientId = ForeignKeyField(IngredientModel, backref="recipe")  # ID of the ingredient

    class Meta:
        database = database
        table_name = "favoriteRecipe"

class MenuRecipe(Model):
    """Model representing the relationship between menus and recipes."""
    menuId = ForeignKeyField(MenuModel, backref="recipe")  # ID of the associated menu
    recipeId = ForeignKeyField(RecipeModel, backref="menu")  # ID of the associated recipe

    class Meta:
        database = database
        table_name = "menuRecipe"

class GroupModel(Model):
    """Model representing a group of users."""
    id = AutoField(primary_key=True)            # Unique identifier for the group
    name = CharField(max_length=50)             # Name of the group
    adminId = ForeignKeyField(UserModel, backref="user")  # ID of the group's administrator
    weeklyMenuId = ForeignKeyField(WeeklyMenuModel, backref="weeklyMenu")  # ID of the associated weekly menu

    class Meta:
        database = database
        table_name = "group"

class GroupMembers(Model):
    """Model representing the relationship between groups and members."""
    groupId = ForeignKeyField(GroupModel, backref="user")  # ID of the associated group
    userId = ForeignKeyField(UserModel, backref="group")    # ID of the associated user

    class Meta:
        database = database
        table_name = "menuRecipe"

class CommentModel(Model):
    """Model representing a comment."""
    id = AutoField(primary_key=True)            # Unique identifier for the comment
    recipeId = ForeignKeyField(RecipeModel, backref="comments")  # ID of the commented recipe
    userId = ForeignKeyField(UserModel, backref="comments")      # ID of the user who commented
    content = TextField()                        # Content of the comment
    rating = IntegerField()                      # Rating of the comment
    datePosted = CharField(max_length=10)       # Date the comment was posted

    class Meta:
        database = database
        table_name = "comment"
