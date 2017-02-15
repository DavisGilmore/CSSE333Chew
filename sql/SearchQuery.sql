USE NWindmiliteja1710
GO


Alter PROCEDURE SearchRecipe
@RecipeName varchar(50)='', @Calories[int]=0, @Time[int]=0

AS

If(@Calories<0 or @Time<0)Begin
	RaisERROR('Caloies and Time cannot be less than 1',10,1);
	Return -1;
End



IF(@Time!=0 and @Calories!=0)
Begin

Select *
From EMPLOYEE
Where (Employee.Fname  like '%_'+@RecipeName+'_%' or Employee.Fname  like @RecipeName+'_%'or Employee.Fname like '%_'+@RecipeName) and EMPLOYEE.Salary<=@Calories and EMPLOYEE.DNO<=@Time*1.2
ORDER BY EMPLOYEE.Salary ASC;
END

Else IF(@Time!=0)
Begin

Select *
From EMPLOYEE
Where (Employee.Fname  like '%_'+@RecipeName+'_%' or Employee.Fname  like @RecipeName+'_%'or Employee.Fname like '%_'+@RecipeName or @RecipeName=EMPLOYEE.Fname) and EMPLOYEE.DNO<=@Time*1.2
ORDER BY EMPLOYEE.Salary ASC;
END

Else IF(@Calories!=0)
Begin

Select *
From EMPLOYEE
Where (Employee.Fname  like '%_'+@RecipeName+'_%' or Employee.Fname  like @RecipeName+'_%'or Employee.Fname like '%_'+@RecipeName or @RecipeName=EMPLOYEE.Fname) and EMPLOYEE.Salary<=@Calories
ORDER BY EMPLOYEE.Salary ASC;
END

ELSE
Begin

Select *
From EMPLOYEE
Where (Employee.Fname  like '%_'+@RecipeName+'_%' or Employee.Fname  like @RecipeName+'_%' or Employee.Fname like '%_'+@RecipeName or @RecipeName=EMPLOYEE.Fname)
ORDER BY EMPLOYEE.Salary ASC;
END