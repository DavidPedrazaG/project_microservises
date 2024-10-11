from sqlalchemy import Column, Integer, String, ForeignKey, Text, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.settings import DATABASE

Base = declarative_base()

# pylint: disable=too-few-public-methods

# Database models

class CommentModel(Base):
    """Model for recipe comments."""
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    recipeId = Column(Integer, ForeignKey('recipe.id'))
    userId = Column(Integer, ForeignKey('user.id'))
    content = Column(Text)
    rating = Column(Integer)
    datePosted = Column(String(10))

    recipe = relationship("RecipeModel", back_populates="comments")
    user = relationship("UserModel", back_populates="comments")


class RecipeModel(Base):
    """Model for recipes."""
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    typeOfFood = Column(String(50))
    preparationTime = Column(Integer)
    nutritionalInfoId = Column(Integer, ForeignKey('nutritionalInfo.id'))
    images = Column(Text)
    preparationProcess = Column(String(50))

    comments = relationship("CommentModel", back_populates="recipe")


class FoodModel(Base):
    """Model for foods."""
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    macronutrientsId = Column(Integer)
    micronutrientsId = Column(Integer)


class GroupModel(Base):
    """Model for user groups."""
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    adminId = Column(Integer, ForeignKey('user.id'))
    weeklyMenuId = Column(Integer, ForeignKey('weeklyMenu.id'))


class IngredientModel(Base):
    """Model for ingredients."""
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    foodId = Column(Integer, ForeignKey('food.id'))
    quantity = Column(Integer)
    measurementUnit = Column(String(50))
    expirationDate = Column(String(50))
    measure = Column(Integer)  # The name is not changed as requested


class MeasureModel(Base):
    """Model for measures."""
    __tablename__ = 'measure'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class MenuModel(Base):
    """Model for weekly menus."""
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    weeklyMenuId = Column(Integer, ForeignKey('weeklyMenu.id'))
    day = Column(String(10))
    hour = Column(String(20))
    type = Column(String(20))


class MenuHistoryModel(Base):
    """Model for menu history."""
    __tablename__ = 'menuHistory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    weeklyMenuId = Column(Integer, ForeignKey('weeklyMenu.id'))
    dateCreated = Column(String(20))


class NotificationModel(Base):
    """Model for user notifications."""
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    message = Column(String(50))
    dateSent = Column(String(20))
    type = Column(String(20))


class NutritionalInfoModel(Base):
    """Model for nutritional information."""
    __tablename__ = 'nutritionalInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    calories = Column(Integer)
    carbohydrates = Column(Integer)
    proteins = Column(Integer)
    fats = Column(Integer)
    vitamins = Column(String(50))
    minerals = Column(String(50))


class PantryModel(Base):
    """Model for user pantry."""
    __tablename__ = 'pantry'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    ingredientIds = Column(Integer, ForeignKey('ingredient.id'))
    dateLastUpdated = Column(String(50))


class PurchaseHistoryModel(Base):
    """Model for purchase history."""
    __tablename__ = 'purchaseHistory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    ingredientsId = Column(Integer, ForeignKey('ingredient.id'))
    purchaseDate = Column(String(50))


class RecipeSuggestionModel(Base):
    """Model for recipe suggestions."""
    __tablename__ = 'recipeSuggestion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    suggestedRecipeId = Column(Integer, ForeignKey('recipe.id'))
    matchedIngredientId = Column(Integer, ForeignKey('ingredient.id'))
    missingIngredientesId = Column(Integer, ForeignKey('ingredient.id'))
    dateSuggested = Column(String(50))


class RolesModel(Base):
    """Model for user roles."""
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    roleName = Column(String(50))


class ShoppingListModel(Base):
    """Model for shopping lists."""
    __tablename__ = 'shoppingList'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    ingredientId = Column(Integer, ForeignKey('ingredient.id'))
    dateCreated = Column(String(20))


class StoreModel(Base):
    """Model for ingredient stores."""
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    location = Column(String(20))
    inventoryId = Column(Integer, ForeignKey('pantry.id'))


class UserModel(Base):
    """Model for users."""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cc = Column(String(20))
    name = Column(String(50))
    lastName = Column(String(50))
    password = Column(String(50))
    email = Column(String(50))
    phoneNumber = Column(String(50))
    role = Column(Integer)


class UserPreferencesModel(Base):
    """Model for user preferences."""
    __tablename__ = 'userPreferences'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'))
    dietaryRestrictions = Column(String(50))
    preferredCuisines = Column(String(50))
    allergens = Column(String(50))


class WeeklyMenuModel(Base):
    """Model for weekly menus."""
    __tablename__ = 'weeklyMenu'
    id = Column(Integer, primary_key=True, autoincrement=True)


class FavoriteRecipeModel(Base):
    """Model for users' favorite recipes."""
    __tablename__ = 'favoriteRecipe'
    userId = Column(Integer, ForeignKey('user.id'), primary_key=True)
    recipeId = Column(Integer, ForeignKey('recipe.id'), primary_key=True)


class RecipeIngredientModel(Base):
    """Model for recipe ingredients."""
    __tablename__ = 'recipeIngredient'
    recipeId = Column(Integer, ForeignKey('recipe.id'), primary_key=True)
    ingredientId = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)


class MenuRecipeModel(Base):
    """Model for recipes in menus."""
    __tablename__ = 'menuRecipe'
    menuId = Column(Integer, ForeignKey('menu.id'), primary_key=True)
    recipeId = Column(Integer, ForeignKey('recipe.id'), primary_key=True)


class GroupMembersModel(Base):
    """Model for group members."""
    __tablename__ = 'groupMembers'
    groupId = Column(Integer, ForeignKey('group.id'), primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'), primary_key=True)

# Database configuration
DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)

# Create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Database session generator."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
