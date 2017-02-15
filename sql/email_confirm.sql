CREATE PROCEDURE [email_confirm]
(@Email [varchar])
AS
SELECT EmailAddress
	FROM UserInfo
	WHERE UserInfo.EmailAddress = @Email