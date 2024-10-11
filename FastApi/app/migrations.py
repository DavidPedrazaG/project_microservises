from sqlalchemy import Column, Integer, String, ForeignKey, Text, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE

Base = declarative_base()

# CommentModel
class CommentModel(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    recipeId = Column(Integer, ForeignKey('recipe.id'))
    userId = Column(Integer, ForeignKey('user.id'))
    content = Column(Text)
    rating = Column(Integer)
    datePosted = Column(String(10))

    recipe = relationship("RecipeModel", back_populates="comments")
    user = relationship("UserModel", back_populates="comments")


# RecipeModel
class RecipeModel(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    typeOfFood = Column(String(50))
    preparationTime = Column(Integer)
    nutritionalInfoId = Column(Integer, ForeignKey('nutritionalInfo.id'))
    images = Column(Text)
    preparationProcess = Column(String(50))

    comments = relationship("CommentModel", back_populates="recipe")


# FoodModel
class FoodModel(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    macronutrientsId = Column(Integer)
    micronutrientsId = Column(Integer)


# GroupModel
class GroupModel(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    adminId = Column(Integer, ForeignKey('user.id'))
    weeklyMenuId = Column(Integer, ForeignKey('weeklyMenu.id'))


# IngredientModel
class IngredientModel(Base):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    foodId = Column(Integer, ForeignKey('food.id'))
    quantity = Column(Integer)
    measurementUnit = Column(String(50))
    expirationDate = Column(String(50))
    meassure = Column(Integer)


# MeasureModel
class MeasureModel(Base):
    __tablename__ = 'measure'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


# MenuModel
class MenuModel(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    weeklyMenuId = Column(Integer, ForeignKey('weeklyMenu.id'))
    day = Column(String(10))
    hour = Column(String(20))
    type = Column(String(20))


# MenuHistoryModel
class MenuHistoryModel(Base):
    __tablename__ = 'menuHistory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    weeklyMenuId = Column(Integer, ForeignKey('weeklyMenu.id'))
    dateCreated = Column(String(20))


# NotificationModel
class NotificationModel(Base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    message = Column(String(50))
    dateSent = Column(String(20))
    type = Column(String(20))


# NutritionalInfoModel
class NutritionalInfoModel(Base):
    __tablename__ = 'nutritionalInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    calories = Column(Integer)
    carbohydrates = Column(Integer)
    proteins = Column(Integer)
    fats = Column(Integer)
    vitamins = Column(String(50))
    minerals = Column(String(50))


# PantryModel
class PantryModel(Base):
    __tablename__ = 'pantry'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    ingredientIds = Column(Integer, ForeignKey('ingredient.id'))
    dateLastUpdated = Column(String(50))


# PurchaseHistoryModel
class PurchaseHistoryModel(Base):
    __tablename__ = 'purchaseHistory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    ingredientsId = Column(Integer, ForeignKey('ingredient.id'))
    purchaseDate = Column(String(50))


# RecipeSuggestionModel
class RecipeSuggestionModel(Base):
    __tablename__ = 'recipeSuggestion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    suggestedRecipeId = Column(Integer, ForeignKey('recipe.id'))
    matchedIngredientId = Column(Integer, ForeignKey('ingredient.id'))
    missingIngredientesId = Column(Integer, ForeignKey('ingredient.id'))
    dateSuggested = Column(String(50))


# RolesModel
class RolesModel(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    roleName = Column(String(50))


# ShoppingListModel
class ShoppingListModel(Base):
    __tablename__ = 'shoppingList'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    ingredientId = Column(Integer, ForeignKey('ingredient.id'))
    dateCreated = Column(String(20))


# StoreModel
class StoreModel(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    location = Column(String(20))
    inventoryId = Column(Integer, ForeignKey('pantry.id'))


# UserModel
class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cc = Column(String(20))
    name = Column(String(50))
    lastName = Column(String(50))
    password = Column(String(50))
    email = Column(String(50))
    phoneNumber = Column(String(50))
    role = Column(Integer)


# UserPreferencesModel
class UserPreferencesModel(Base):
    __tablename__ = 'userPreferences'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    dietaryRestrictions = Column(String(50))
    preferredCuisines = Column(String(50))
    allergens = Column(String(50))


# WeeklyMenuModel
class WeeklyMenuModel(Base):
    __tablename__ = 'weeklyMenu'
    id = Column(Integer, primary_key=True, autoincrement=True)


# FavoriteRecipeModel
class FavoriteRecipeModel(Base):
    __tablename__ = 'favoriteRecipe'
    userId = Column(Integer, ForeignKey('user.id'), primary_key=True)
    recipeId = Column(Integer, ForeignKey('recipe.id'), primary_key=True)


# RecipeIngredientModel
class RecipeIngredientModel(Base):
    __tablename__ = 'recipeIngredient'
    recipeId = Column(Integer, ForeignKey('recipe.id'), primary_key=True)
    ingredientId = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)


# MenuRecipeModel
class MenuRecipeModel(Base):
    __tablename__ = 'menuRecipe'
    menuId = Column(Integer, ForeignKey('menu.id'), primary_key=True)
    recipeId = Column(Integer, ForeignKey('recipe.id'), primary_key=True)


# GroupMembersModel
class GroupMembersModel(Base):
    __tablename__ = 'groupMembers'
    groupId = Column(Integer, ForeignKey('group.id'), primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'), primary_key=True)

DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)


# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()