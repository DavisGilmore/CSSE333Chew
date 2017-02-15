CREATE PROCEDURE [get_steps]
(@RID [varchar])
AS
SELECT *
	FROM Step
	WHERE RecipeID = @RID