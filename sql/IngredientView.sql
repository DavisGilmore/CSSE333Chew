Create View RecipeIngredients
AS
Select  Name, Unit, Amount,  IngredientName
From (Select  Name, Unit, Amount, IngredientID
	  From [Recipe]
	Inner Join RecipeHasIngredient
	ON Recipe.RecipeID=RecipeHasIngredient.RecipeID) as A
Inner Join Ingredient
ON Ingredient.IngredientID= A.IngredientID