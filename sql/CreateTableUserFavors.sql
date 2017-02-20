Create Table UserFavorRecipe
(

	EmailAddress varchar(50) NOT NULL,
	RecipeID int NOT NULL,

	Primary KEY (EmailAddress,RecipeID),
	Foreign KEY(EmailAddress) References UserInfo(EmailAddress),
	Foreign KEY(RecipeID) References Recipe(RecipeID)


);
