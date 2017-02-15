CREATE PROCEDURE [favors]
(@RecipeID [varchar],
 @Email [varchar])
AS
IF(NOT EXISTS(SELECT * FROM UserInfo WHERE UserInfo.EmailAddress = @Email))
BEGIN
	RAISERROR('invalid email address',10,1);
	RETURN 1;
END
IF(NOT EXISTS(SELECT * FROM Recipe WHERE Recipe.RecipeID = @RecipeID))
BEGIN
	RAISERROR('invalid recipe id',10,1);
	RETURN 2;
END
IF (EXISTS(SELECT * FROM UserFavorsRecipe WHERE UserFavorsRecipe.RecipeID = @RecipeID AND UserFavorsRecipe.EmailAddress = @Email))
BEGIN
	RAISERROR('recipe already favored', 10, 1);
	RETURN 3;
END
INSERT INTO UserFavorsRecipe (EmailAddress, RecipeID)
VALUES (@Email, @RecipeID)
RETURN 0;