Create Table RecipeUsesTool
(

	
	RecipeID int NOT NULL,
	ToolID int NOT NULL,


	Primary KEY (RecipeID,ToolID),
	Foreign KEY(ToolID) References Tool(ToolID),
	Foreign KEY(RecipeID) References Recipe(RecipeID)


);
