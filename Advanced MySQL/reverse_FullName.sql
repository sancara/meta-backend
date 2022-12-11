 UPDATE Employees SET ReverseFullName = CONCAT(SUBSTRING_INDEX(FullName, ' ', -1), ' ', SUBSTRING_INDEX(FullName, ' ', 1));
