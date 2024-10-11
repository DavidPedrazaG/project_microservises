"""
Main application module for the FastAPI project.

This module sets up the FastAPI application, manages the database connection
and table creation, and includes the route definitions.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config.database import database as connection
#                         CommentModel, RecipeModel, FoodModel,
#                         GroupModel,IngredientModel,MeasureModel,MenuModel,MenuHistoryModel,
#                         NotificationModel,NutritionalInfoModel,PantryModel,PurchaseHistoryModel,
#                         RecipeSuggestionModel,RolesModel,ShoppingListModel,StoreModel,UserModel,
#                         UserPreferencesModel,WeeklyMenuModel,FavoriteRecipe,RecipeIngredient,
#                         MenuRecipe,GroupMembers)
from routes.user import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager for the application's lifespan.

    Connects to the database, creates tables if needed, and ensures
    proper closure of the database connection on shutdown.
    """
    if connection.is_closed():
        connection.connect()
        # connection.create_tables([
        #     CommentModel, RecipeModel, FoodModel,
        #                 GroupModel,IngredientModel,MeasureModel,MenuModel,MenuHistoryModel,
        #                 NotificationModel,NutritionalInfoModel,PantryModel,PurchaseHistoryModel,
        #                 RecipeSuggestionModel,RolesModel,ShoppingListModel,StoreModel,UserModel,
        #                 UserPreferencesModel,WeeklyMenuModel,FavoriteRecipe,RecipeIngredient,
        #                 MenuRecipe,GroupMembers
        # ])

    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/", include_in_schema=True)
async def root():
    return RedirectResponse("/docs")

app.include_router(router, prefix="/api/user", tags=["user"])