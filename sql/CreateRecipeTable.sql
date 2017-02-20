
Create Table Recipe
(
	RecipeID int NOT NULL,
	Name  varchar(80) NOT NULL,
	TypeOfRecipie varchar(20),
	Origin varchar(30),
	TimeToCook int Not NULL Check (TimeToCook>0),
	Calorie int Not NULL Check (Calorie>0),
	

	Primary KEY(RecipeID)


);
