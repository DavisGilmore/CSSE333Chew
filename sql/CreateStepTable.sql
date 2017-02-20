Create Table Step
(

	StepNumber int NOT NULL,
	RecipeID int NOT NULL,
	[Description] varchar(max) Not NULL, 

	Primary KEY (StepNumber,RecipeID),
	Foreign KEY(RecipeID) References Recipe(RecipeID)


);
