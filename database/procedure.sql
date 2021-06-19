USE Ticket_reservation
GO
-- 为订单添加出行人并生成票号，若表中无此出行人，则同时添加到出行人表
CREATE PROCEDURE [Add_Passenger] (
    @Uname varchar(20),
    @IDCard_NO char(18),
    @Order_id char(12),
    @Pname varchar(30),
    @Ticket_NO char(13) OUTPUT
)
AS
BEGIN
    DECLARE @Flight_NO char(6),
            @Title char(9),
            @Pname_tmp varchar(30);
    
    SELECT @Pname_tmp = [Pname]
    FROM [Passenger]
    WHERE [IDCard_NO] = @IDCard_NO 
    AND [Uname] = @Uname; 
    
    IF @Pname_tmp IS NOT NULL
    BEGIN
        IF @Pname_tmp <> @Pname
            RETURN 0;
    END
    ELSE
    BEGIN
        INSERT INTO [Passenger] 
            VALUES(@Uname,@IDCard_NO,@Pname);
        
        IF @@error <> 0 OR @@rowcount <> 1
            RETURN 0;
    END

    SELECT  @Flight_NO = [Flight_NO]
    FROM [Itinerary]
    WHERE [Itinerary_id] = ( 
        SELECT [Itinerary_id]
        FROM [Order]
        WHERE [Order_id] = @Order_id); 

    SET @Title = LEFT(@Flight_NO, 3) + LEFT(@Order_id, 6);

    SELECT @Ticket_NO = @Title + RIGHT(10001 + ISNULL(RIGHT(MAX([Ticket_NO]), 4), 0), 4)
    FROM [Order_Passenger]
    WHERE [Ticket_NO] LIKE (@Title + '%');

    INSERT INTO [Order_Passenger]([Uname], [IDCard_NO], [Order_id], [Ticket_NO])
        VALUES(@Uname, @IDCard_NO, @Order_id, @Ticket_NO);
    
    IF @@error <> 0 OR @@rowcount <> 1
        RETURN 0;
    
    RETURN 1;
END
GO
-- 创建订单，根据创建时间生成订单号
CREATE PROCEDURE [Create_Order] (
        @Order_pay int,
        @Passenger People READONLY,
        @Contact_Phone char(11),
        @Itinerary_id char(12),
        @Cabin_code char(1),
        @Uname varchar(20),
        @Order_id char(12) OUTPUT
)
AS
BEGIN
    DECLARE @Currenttime CHAR(6),
            @Plane_NO char(10),
            @Ticker_num smallint;

    DECLARE @IDCard_NO char(18),
            @Pname varchar(30);

    DECLARE [Cur_Passenger] CURSOR 
    FOR SELECT [IDCard_NO],[Pname]
        FROM @Passenger;

    OPEN [Cur_Passenger];

    FETCH NEXT FROM [Cur_Passenger] INTO @IDCard_NO, @Pname;

    SET @Ticker_num = 0;

    WHILE @@fetch_status = 0
    BEGIN
        IF @Pname <> (SELECT [Pname]
                      FROM [Passenger]
                      WHERE [IDCard_NO] = @IDCard_NO 
                      AND [Uname] = @Uname)
        BEGIN
            CLOSE [Cur_Passenger];
            DEALLOCATE [Cur_Passenger];
            RETURN 0;
        END
        FETCH NEXT FROM [Cur_Passenger] INTO @IDCard_NO, @Pname;

        SET @Ticker_num = @Ticker_num +1;
    END

    CLOSE [Cur_Passenger];

    SET @Currenttime = CONVERT(CHAR(6), GETDATE(), 12);
    
    SELECT @Plane_NO=[Plane_NO] 
    FROM [Itinerary] 
    WHERE [Itinerary_id]=@Itinerary_id;

    SELECT @Order_id = @Currenttime + RIGHT(1000001 + ISNULL(RIGHT(MAX([Order_id]), 6), 0), 6)
    FROM [Order]
    WHERE [Order_id] like (@Currenttime+'%');

    BEGIN TRANSACTION

    INSERT INTO [Order]
        VALUES(@Order_id, @Order_pay, @Ticker_num, @Contact_Phone, @Itinerary_id, @Plane_NO, @Cabin_code, @Uname, GETDATE(), '未支付');
    
    IF @@error <> 0 OR @@rowcount <> 1
    BEGIN
        ROLLBACK TRANSACTION
        RETURN 0;
    END
        
    
    OPEN [Cur_Passenger];

    FETCH NEXT FROM [Cur_Passenger] INTO @IDCard_NO, @Pname;

    WHILE @@fetch_status = 0
    BEGIN
        DECLARE @result int,
                @Ticket_NO char(13);
        EXEC @result  = [Add_Passenger] @Uname, @IDCard_NO,@Order_id,@Pname,@Ticket_NO OUTPUT;

        IF @@error <> 0 OR @@rowcount <> 1
        BEGIN
            CLOSE [Cur_Passenger];
            DEALLOCATE [Cur_Passenger];
            ROLLBACK TRANSACTION;
            RETURN 0;
        END

        FETCH NEXT FROM [Cur_Passenger] INTO @IDCard_NO, @Pname;
    END

    CLOSE [Cur_Passenger];
    DEALLOCATE [Cur_Passenger];
    COMMIT TRANSACTION;

    RETURN 1;
END
GO
-- 创建行程，根据行程的日期自动生成行程号
CREATE PROCEDURE [Create_Itinerary] (
    @Plan_departuretime datetime,
    @Plan_arrivaltime datetime,
    @Plan_departuredate date,
    @Flight_NO char(6),
    @Plane_NO char(10),
    @Itinerary_id char(12) OUTPUT
)
AS
BEGIN
    DECLARE @Currenttime CHAR(6);

    SET @Currenttime = CONVERT(CHAR(6), @Plan_departuredate, 12);

    SELECT @Itinerary_id = @Currenttime + RIGHT(1000001 + ISNULL(RIGHT(MAX([Itinerary_id]), 6), 0), 6)
    FROM [Itinerary]
    WHERE [Plan_departuredate] = @Plan_departuredate;

    INSERT INTO [Itinerary]
        VALUES(@Itinerary_id, @Plan_departuretime, @Plan_arrivaltime, @Plan_departuredate, @Flight_NO, @Plane_NO, @Plan_departuretime, @Plan_arrivaltime, '航班计划', 0);

    IF @@error <> 0 OR @@rowcount <> 1
        RETURN 0;
    
    RETURN 1;
END

