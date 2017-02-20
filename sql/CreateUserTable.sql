Create Table UserInfo
(

	EmailAddress varchar(50) NOT NULL,
	Username varchar(20) NOT NULL Unique,
	FirstName varchar(20) NOT NULL,
	LastName varchar(35) NOT NULL,

	Primary KEY(EmailAddress)


);
