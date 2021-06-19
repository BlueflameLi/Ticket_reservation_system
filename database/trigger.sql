USE Ticket_reservation
GO
-- 取消订单或退票时更新余票
CREATE TRIGGER [ADD_Seat_remaining]
	ON [Order]
	AFTER UPDATE
AS
IF UPDATE([Order_status])
BEGIN
    DECLARE @Order_status char(10),
            @Order_status_old char(10),
            @Itinerary_id char(12),
            @Cabin_code char(1),
            @num smallint;

    DECLARE [Cur_inserted] CURSOR 
    FOR SELECT [Order_status],[Itinerary_id],[Cabin_code],[Ticker_num]
        FROM inserted;
    DECLARE [Cur_deleted] CURSOR 
    FOR SELECT [Order_status]
        FROM deleted;
    OPEN [Cur_inserted];
    OPEN [Cur_deleted];

    FETCH NEXT FROM [Cur_inserted] INTO @Order_status, @Itinerary_id,@Cabin_code,@num;
    FETCH NEXT FROM [Cur_deleted] INTO @Order_status_old;

    WHILE @@fetch_status = 0 
    BEGIN
        IF @Order_status_old IN ('已退票','已取消')
        BEGIN
            DECLARE @error_mes varchar(1000);
	    	SET @error_mes='订单已失效';
	    	RAISERROR(@error_mes,16,1);
	    	ROLLBACK;
        END
        ELSE IF @Order_status IN ('已退票','已取消')
        BEGIN
            UPDATE [Itinerary_Cabin]
	    	SET [remaining] = [remaining] + @num
	    	WHERE [Itinerary_id] = @Itinerary_id
            AND [Cabin_code] = @Cabin_code
        END

        FETCH NEXT FROM [Cur_inserted] INTO @Order_status, @Itinerary_id,@Cabin_code,@num;
        FETCH NEXT FROM [Cur_deleted] INTO @Order_status_old;
    END

    CLOSE [Cur_inserted];
    CLOSE [Cur_deleted];

    DEALLOCATE [Cur_inserted];
    DEALLOCATE [Cur_deleted];
    
END
GO
-- 预定机票更新余票
CREATE TRIGGER [SUB_Seat_remaining]
	ON [Order]
	AFTER INSERT
AS
BEGIN
    DECLARE @num smallint;
    
    SELECT @num = [Ticker_num] 
    FROM inserted;

    IF (SELECT [remaining] 
        FROM [Itinerary_Cabin]
		WHERE [Itinerary_id] = (SELECT [Itinerary_id] FROM inserted)
        AND [Cabin_code] = (SELECT [Cabin_code] FROM inserted)) < @num
    BEGIN
        DECLARE @error_mes varchar(1000);
		SET @error_mes='余票不足';
		RAISERROR(@error_mes,16,1);
		ROLLBACK;
    END
    ELSE
    BEGIN
        UPDATE [Itinerary_Cabin]
		SET [remaining] = [remaining] - @num
		WHERE [Itinerary_id] = (SELECT [Itinerary_id] FROM inserted) 
        AND [Cabin_code] = (SELECT [Cabin_code] FROM inserted)
    END

END
GO
--航班动态-删除
CREATE TRIGGER [Itinerary_Delete]
	ON [Flights]
	INSTEAD OF DELETE
AS
	UPDATE [Itinerary]
	SET [Flight_status] = '航班取消'
	WHERE [Itinerary_id] IN (SELECT [Itinerary_id] FROM inserted)
GO
--余票不能大于座位
CREATE TRIGGER [Seat_manage]
	ON [Itinerary_Cabin]
	AFTER UPDATE
AS
BEGIN
    IF UPDATE([Remaining])
    BEGIN
        DECLARE @Remaining int,
                @Plane_NO char(10),
                @Cabin_code char(1);
        
        DECLARE [Cur_UPDATE] CURSOR 
        FOR SELECT [Remaining],[Plane_NO],[Cabin_code]
        FROM inserted;

        OPEN [Cur_UPDATE];

        FETCH NEXT FROM [Cur_UPDATE] INTO @Remaining, @Plane_NO,@Cabin_code;

        WHILE @@fetch_status = 0 
        BEGIN
	        IF  @Remaining > (SELECT [Seat_capacity] 
                              FROM [Cabin]
	        	              WHERE [Plane_NO] = @Plane_NO 
                              AND [Cabin_code] = @Cabin_code)
            BEGIN
	        	DECLARE @error_mes varchar(1000)  
	        	SET @error_mes='余票不能大于飞机座位！'
                CLOSE [Cur_UPDATE];
                DEALLOCATE [Cur_UPDATE];
	        	RAISERROR(@error_mes,16,1)  
	        	ROLLBACK;
            END
            FETCH NEXT FROM [Cur_UPDATE] INTO @Remaining, @Plane_NO,@Cabin_code;
        END
        CLOSE [Cur_UPDATE];
        DEALLOCATE [Cur_UPDATE];
    END
END
GO
