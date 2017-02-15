CREATE PROCEDURE [get_recipe_name]
(@RecipeID [varchar])
AS
SELECT Recipe.Name
	FROM Recipe
	WHERE RecipeID = @RecipeID