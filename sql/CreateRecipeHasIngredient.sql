Create Table RecipeHasIngredient
(

	
	RecipeID int NOT NULL,
	IngredientID int NOT NULL,
	Unit varchar(10) NOT NUll,
	Amount varchar(20) NOT NULL,
	AdditionalDescription varchar(max),


	Primary KEY (RecipeID,IngredientID),
	Foreign KEY(IngredientID) References Ingredient(IngredientID),
	Foreign KEY(RecipeID) References Recipe(RecipeID)


);
