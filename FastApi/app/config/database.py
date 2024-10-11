"""
Module for defining database models using the Peewee ORM.
"""
from dotenv import load_dotenv
from peewee import *
from config.settings import DATABASE

load_dotenv()

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)

class UserModel(Model):
    id = AutoField(primary_key=True)
    cc = CharField(max_length=20)
    name = CharField(max_length=50)
    lastName = CharField(max_length=50)
    password = CharField(max_length=50)
    email = CharField(max_length=50)
    phoneNumber = CharField(max_length=50)
    role = IntegerField()
    

    class Meta:
        database = database
        table_name = "user"

class RecipeModel(Model):
    """Model representing a Recipe."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    typeOfFood = CharField(max_length=50)
    preparationTime = IntegerField()
    nutritionalInfoId = IntegerField()
    images = TextField()
    preparationProcess = CharField(max_length=50)
    

    class Meta:
        """Class defining properties of the RecipeModel."""
        database = database
        table_name = "recipe"



class FoodModel(Model):
    """Model representing an Food."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    macronutrientsId =  IntegerField()
    micronutrientsId = IntegerField()

    class Meta:
        """Class defining properties of the Food model."""
        database = database
        table_name = "food"

class IngredientModel(Model):
    """Model representing a book."""
    id = AutoField(primary_key=True)
    foodId = ForeignKeyField(FoodModel, backref="food")
    quantity = IntegerField()
    measurementUnit = CharField(max_length=50)
    expirationDate = CharField(max_length=50)
    meassure = IntegerField()
    
    

    class Meta:
        """Class defining properties of the BookModel."""
        database = database
        table_name = "ingredient"

 
class MeasureModel(Model):
    """Model representing the relationship between authors and books."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)

    class Meta:
        """Class defining properties of the AuthorBook model."""
        database = database
        table_name = "measure"

class NotificationModel(Model):
    id = AutoField(primary_key=True)
    userId = ForeignKeyField(UserModel, backref="user")
    message = CharField(max_length=50)
    dateSent = CharField(max_length=20)
    type = CharField(max_length=20)

    class Meta:

        database = database
        table_name = "notification"



class NutritionalInfoModel(Model):
    id = AutoField(primary_key=True)
    calories = IntegerField()
    carbohydrates = IntegerField()
    proteins = IntegerField()
    fats = IntegerField
    vitamins = CharField(max_length=50)
    minerals = CharField(max_length=50)

    class Meta:

        database = database
        table_name = "nutritionalInfo"



class PantryModel(Model):
    id = AutoField(primary_key=True)
    userId = ForeignKeyField(UserModel, backref="user")
    ingredientIds = ForeignKeyField(IngredientModel, backref="ingredient")
    dateLastUpdated = CharField(max_length=50)
   

    class Meta:

        database = database
        table_name = "pantry"



class PurchaseHistoryModel(Model):
    id = AutoField(primary_key=True)
    userId = ForeignKeyField(UserModel, backref="user")
    ingredientsId = ForeignKeyField(IngredientModel, backref="ingredient")
    purchaseDate = CharField(max_length=50)

    class Meta:

        database = database
        table_name = "purchaseHistory"



class RecipeSuggestionModel(Model):
    id = AutoField(primary_key=True)
    userId = ForeignKeyField(UserModel, backref="books")
    suggestedRecipeId = ForeignKeyField(RecipeModel, backref="books")
    matchedIngredientId= ForeignKeyField(IngredientModel, backref="ingredient")
    missingIngredientesId = ForeignKeyField(IngredientModel, backref="ingredient")
    dateSuggested = CharField(max_length=50)


    class Meta:

        database = database
        table_name = "recipeSuggestion"

class RolesModel(Model):
    id = AutoField(primary_key=True)
    roleName = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "roles"


class ShoppingListModel(Model):
    id = AutoField(primary_key=True)
    userId = ForeignKeyField(UserModel, backref="books")
    ingredientId = ForeignKeyField(IngredientModel,backref="books")
    dateCreated = CharField(max_length=20)

    class Meta:
        database = database
        table_name = "shoppingList"

 
class StoreModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    location = CharField(max_length=20)
    inventoryId = ForeignKeyField(PantryModel,backref="pantry")

    class Meta:
        database = database
        table_name = "store"


class UserPreferencesModel(Model):
    id = AutoField(primary_key=True)
    userId = ForeignKeyField(UserModel, backref="user")
    dietaryRestrictions = CharField(max_length=50)
    preferredCuisines = CharField(max_length=50)
    allergens = CharField(max_length=50)
    
    

    class Meta:
        database = database
        table_name = "userPreferences"

class WeeklyMenuModel(Model):
    id = AutoField(primary_key=True)

    class Meta:
        database = database
        table_name = "weeklyMenu"

class MenuHistoryModel(Model):
    id = AutoField(primary_key=True)
    userId = ForeignKeyField(UserModel, backref="user")
    weeklyMenuId = ForeignKeyField(WeeklyMenuModel, backref="weeklyMenu")
    dateCreated = CharField(max_length=20)

    class Meta:

        database = database
        table_name = "menuHistory"
        
class MenuModel(Model):
    """Model representing the relationship between cameras and cellphones."""
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
    userId = ForeignKeyField(UserModel, backref="recipes")
    recipeId = ForeignKeyField(RecipeModel, backref="users")

    class Meta:
        database = database
        table_name = "favoriteRecipe"

class RecipeIngredient(Model):
    recipeId = ForeignKeyField(RecipeModel, backref="ingredient")
    ingredientId = ForeignKeyField(IngredientModel, backref="recipe")

    class Meta:
        database = database
        table_name = "favoriteRecipe"

class MenuRecipe(Model):
    menuId = ForeignKeyField(MenuModel,backref="recipe")
    recipeId = ForeignKeyField(RecipeModel,backref="menu")

    class Meta:
        database = database
        table_name = "menuRecipe"


class GroupModel(Model):
    """Model representing a book."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    adminId = ForeignKeyField(UserModel, backref="user")
    weeklyMenuId = ForeignKeyField(WeeklyMenuModel, backref="weeklyMenu")
    

    class Meta:
        """Class defining properties of the BookModel."""
        database = database
        table_name = "group"

class GroupMembers(Model):
    groupId = ForeignKeyField(GroupModel,backref="user")
    userId = ForeignKeyField(UserModel,backref="group")

    class Meta:
        database = database
        table_name = "menuRecipe"
class CommentModel(Model):
    """Model representing a Comment."""
    id = AutoField(primary_key=True)
    recipeId = ForeignKeyField(RecipeModel, backref="comments")  
    userId = ForeignKeyField(UserModel, backref="comments")  
    content = TextField()
    rating = IntegerField()
    datePosted = CharField(max_length=10)

    class Meta:
        database = database
        table_name = "comment"