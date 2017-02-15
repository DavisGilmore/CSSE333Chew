CREATE PROCEDURE [get_favored_recipes]
(@EmailAddress [varchar])
AS
SELECT Recipe.RecipeID, Recipe.Name
	FROM Recipe, UserFavorsRecipe
	WHERE Recipe.RecipeID = UserFavorsRecipe.RecipeID
		AND UserFavorsRecipe.EmailAddress = @EmailAddress