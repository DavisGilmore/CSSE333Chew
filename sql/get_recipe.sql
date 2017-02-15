CREATE PROCEDURE [get_recipe]
(@RID [varchar])
AS
SELECT *
	FROM Recipe
	WHERE RecipeID = @RID