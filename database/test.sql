USE Ticket_reservation 
GO
INSERT INTO [User]([Uname], [Passwd])
VALUES  ('admin','123456')
GO
INSERT INTO [Airport]
VALUES  ('SHA','上海','虹桥'),
        ('BJS','北京','首都')
GO
INSERT INTO [Flight]
VALUES  ('MU5099','SHA','BJS','T2','T2','东方航空')
GO
INSERT INTO [Airplane]
VALUES  ('B-1234','波音 777-300','宽体')
GO
INSERT INTO [Cabin]
VALUES  ('B-1234','A','头等舱',10),
        ('B-1234','B','公务舱',20),
        ('B-1234','C','公务舱',20),
        ('B-1234','D','公务舱',20),
        ('B-1234','E','公务舱',20),
        ('B-1234','F','公务舱',20),
        ('B-1234','G','公务舱',20),
        ('B-1234','H','经济舱',30),
        ('B-1234','I','经济舱',30),
        ('B-1234','J','经济舱',30),
        ('B-1234','K','经济舱',30),
        ('B-1234','L','经济舱',30),
        ('B-1234','M','经济舱',30),
        ('B-1234','N','经济舱',30),
        ('B-1234','O','经济舱',30),
        ('B-1234','P','经济舱',30),
        ('B-1234','Q','经济舱',30),
        ('B-1234','R','经济舱',30),
        ('B-1234','S','经济舱',30),
        ('B-1234','T','经济舱',30)
GO
DECLARE @Itinerary_id char(12);
EXEC [Create_Itinerary] '2021-06-19 7:00:00','2021-06-19 9:15:00','2021-06-19','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-18 7:00:00','2021-06-18 9:15:00','2021-06-18','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-27 7:00:00','2021-06-27 9:15:00','2021-06-27','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-26 7:00:00','2021-06-26 9:15:00','2021-06-26','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-25 7:00:00','2021-06-25 9:15:00','2021-06-25','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-24 7:00:00','2021-06-24 9:15:00','2021-06-24','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-23 7:00:00','2021-06-23 9:15:00','2021-06-23','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-22 7:00:00','2021-06-22 9:15:00','2021-06-22','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-21 7:00:00','2021-06-21 9:15:00','2021-06-21','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-30 7:00:00','2021-06-30 9:15:00','2021-06-30','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-29 7:00:00','2021-06-29 9:15:00','2021-06-29','MU5099', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-28 7:00:00','2021-06-28 9:15:00','2021-06-28','MU5099', 'B-1234',@Itinerary_id OUTPUT;
GO
DECLARE @Itinerary_id char(12);

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-19'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-19 7:53:00',
    [Arrivaltime] = '2021-06-19 9:41:00',
    [Flight_status] ='航班到达',
    [Mileage] = 1088
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30),
        (@Itinerary_id,'B-1234','M',1360,30),
        (@Itinerary_id,'B-1234','O',1050,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-18'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-18 7:23:00',
    [Arrivaltime] = '2021-06-18 9:30:00',
    [Flight_status] ='航班到达',
    [Mileage] = 1088
WHERE @Itinerary_id = [Itinerary_id];

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)


SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-27'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-27 7:13:00',
    [Arrivaltime] = '2021-06-27 9:21:00'
WHERE @Itinerary_id = [Itinerary_id];

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-26'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-26 7:03:00',
    [Arrivaltime] = '2021-06-26 9:31:00'
WHERE @Itinerary_id = [Itinerary_id];

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','G',1630,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30),
        (@Itinerary_id,'B-1234','M',1360,30),
        (@Itinerary_id,'B-1234','N',1180,30),
        (@Itinerary_id,'B-1234','P',1000,30),
        (@Itinerary_id,'B-1234','Q',810,30),
        (@Itinerary_id,'B-1234','R',770,30),
        (@Itinerary_id,'B-1234','S',720,30),
        (@Itinerary_id,'B-1234','T',500,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-25'; 


INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-24'; 


INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-23'; 


INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-22'; 


UPDATE [Itinerary]
SET [Departuretime] = '2021-06-22 7:37:00',
    [Arrivaltime] = '2021-06-22 9:05:00',
    [Flight_status] ='航班到达',
    [Mileage] = 1088
WHERE @Itinerary_id = [Itinerary_id];

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-21'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-21 7:04:00',
    [Arrivaltime] = '2021-06-21 9:19:00',
    [Flight_status] ='航班到达',
    [Mileage] = 1088
WHERE @Itinerary_id = [Itinerary_id];

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-30'; 


INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-29'; 


INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-28'; 


INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-1234','A',7480,10),
        (@Itinerary_id,'B-1234','B',6800,20),
        (@Itinerary_id,'B-1234','C',4910,20),
        (@Itinerary_id,'B-1234','D',4380,20),
        (@Itinerary_id,'B-1234','E',3480,20),
        (@Itinerary_id,'B-1234','F',2690,30),
        (@Itinerary_id,'B-1234','H',1790,30),
        (@Itinerary_id,'B-1234','I',1770,30),
        (@Itinerary_id,'B-1234','J',1680,30),
        (@Itinerary_id,'B-1234','K',1630,30),
        (@Itinerary_id,'B-1234','L',1540,30)
GO
DECLARE @Itinerary_id char(12),
        @Plane_NO char(10)

SELECT @Itinerary_id = [行程号]
FROM [Ticket]
WHERE [航班号1] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-22'
AND [舱位代码]='A'
; 

DECLARE @Order_id char(12),
        @result int,
        @Passenger People;

INSERT INTO @Passenger
VALUES ('330234838204054411','张三'),
       ('440384850283858333','李四')

EXEC @result = [Create_Order] 4000, @Passenger, '13712345678', @Itinerary_id, 'A','admin', @Order_id OUTPUT;
GO
DECLARE @Itinerary_id char(12),
        @Plane_NO char(10)

SELECT @Itinerary_id = [行程号]
FROM [Ticket]
WHERE [航班号1] = 'MU5099' 
AND [Plan_departuredate] = '2021-06-27'
AND [舱位代码]='C';

DECLARE @Order_id char(12),
        @result int,
        @Passenger People;

INSERT INTO @Passenger
VALUES ('330234838204054411','张三'),
       ('420382342283858333','王五')

EXEC @result = [Create_Order] 3000, @Passenger, '13712345678', @Itinerary_id, 'C','admin', @Order_id OUTPUT;

-- GO
-- UPDATE [Order]
-- SET [Order_status] = '已取消';