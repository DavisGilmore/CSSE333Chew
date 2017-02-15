CREATE PROCEDURE [insert_new_user]
(@EmailAddress [varchar],
 @Username [varchar],
 @FirstName [varchar],
 @LastName [varchar])
AS
AS
--DECLARE @match varchar;
--SET @match = '@'
--IF ( NOT (CHARINDEX(@match, @EmailAddress) > 0))
--	BEGIN
--	RAISERROR('invalid email format', 10, 1);
--	RETURN 1;
--	END

IF (EXISTS (SELECT * FROM UserInfo WHERE EmailAddress = @EmailAddress))
	BEGIN
	RAISERROR('email already has account', 10, 1);
	RETURN 2;
	END

IF (EXISTS (SELECT * FROM UserInfo WHERE Username = @Username))
	BEGIN
	RAISERROR('username is already in user', 10, 1);
	RETURN 3;
	END

INSERT INTO UserInfo (EmailAddress, Username, FirstName, LastName)
	VALUES (@EmailAddress, @Username, @FirstName, @LastName)

RETURN 0;