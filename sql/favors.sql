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
	RAISERROR('invalid email address',10,1);
	RETURN 1;
END

INSERT INTO UserFavorsRecipe (EmailAddress, RecipeID)
VALUES (@Email, @RecipeID)
RETURN 0;