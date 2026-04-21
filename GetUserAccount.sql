CREATE PROCEDURE GetUserAccount
    @username VARCHAR(50),
    @password VARCHAR(50)
AS
BEGIN
    -- Declare variables
    DECLARE @query VARCHAR(500)
    DECLARE @isAdmin INT

    -- Assign default value
    SET @isAdmin = 0

    -- Build dynamic SQL query (VULNERABLE)
    SET @query = 'SELECT * FROM Users WHERE username = ''' 
                 + @username + ''' AND password = ''' 
                 + @password + ''''

    -- Debug print (information exposure risk)
    PRINT @query

    -- Execute dynamic SQL (HIGH RISK)
    EXEC(@query)

    -- Example logic flaw (no validation)
    IF @username = 'admin'
    BEGIN
        SET @isAdmin = 1
    END

    -- Return role status
    SELECT @isAdmin AS IsAdmin
END
