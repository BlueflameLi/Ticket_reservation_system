USE Ticket_reservation 
GO
INSERT INTO [Airport]
VALUES  ('SZX','深圳','宝安'),
('HGH','杭州','萧山'),
('CSX','长沙','黄花'),
('PVG','上海','浦东'),
('CAN','广州','白云'),
('CKG','重庆','江北'),
('WUH','武汉','天河'),
('SYX','三亚','凤凰'),
('SIA','西安','咸阳'),
('NKG','南京','禄口'),
('TNA','济南','遥墙'),
('KMG','哈尔滨','太平'),
('CTU','成都','双流')
GO
INSERT INTO [Flight]
VALUES  ('9C8965','SZX','SHA','T3','T1','春秋航空'),
('GJ8006','CTU','HGH','T2','T3','长龙航空'), 
('HU7442','CKG','CAN','T3','T1','海南航空'),
('G54874','HGH','CKG','T3','T2','华夏航空'),
('HO1243','SHA','CKG','T2','T3','吉祥航空'),
('CZ9541','CTU','HGH','T1','T3','南方航空'),
('FM9351','HGH','CAN','T3','T1','上海航空'),
('MU2753','NKG','CSX','T2','T3','东方航空'),
('JD5175','SYX','SIA','T2','T2','首都航空'),
('EU7076','CTU','HGH','T1','T3','成都航空'),
('SC9904','TNA','SZX','T1','T3','山东航空'),
('CA1339','BJS','CAN','T2','T1','中国国航')
GO
INSERT INTO [Airplane]
VALUES
('B-6341','波音 737-800','窄体'),
('C-1234','空中客车A320','窄体'),
('C-2234','空中客车A321','窄体'),
('C-3234','空中客车A350','宽体')
GO
INSERT INTO [Cabin]
VALUES  
        ('B-6341','A','头等舱',10),
        ('B-6341','B','公务舱',20),
        ('B-6341','C','公务舱',20),
        ('B-6341','D','公务舱',20),
        ('B-6341','E','公务舱',20),
        ('B-6341','F','公务舱',20),
        ('B-6341','G','公务舱',20),
        ('B-6341','H','经济舱',30),
        ('B-6341','I','经济舱',30),
        ('B-6341','J','经济舱',30),
        ('B-6341','K','经济舱',30),
        ('B-6341','L','经济舱',30),
        ('B-6341','M','经济舱',30),
        ('B-6341','N','经济舱',30),
        ('B-6341','O','经济舱',30),
        ('B-6341','P','经济舱',30),
        ('B-6341','Q','经济舱',30),
        ('B-6341','R','经济舱',30),
        ('B-6341','S','经济舱',30),
        ('B-6341','T','经济舱',30),
        ('C-1234','A','头等舱',10),
        ('C-1234','B','公务舱',20),
        ('C-1234','C','公务舱',20),
        ('C-1234','D','公务舱',20),
        ('C-1234','E','公务舱',20),
        ('C-1234','F','公务舱',20),
        ('C-1234','G','公务舱',20),
        ('C-1234','H','经济舱',30),
        ('C-1234','I','经济舱',30),
        ('C-1234','J','经济舱',30),
        ('C-1234','K','经济舱',30),
        ('C-1234','L','经济舱',30),
        ('C-1234','M','经济舱',30),
        ('C-1234','N','经济舱',30),
        ('C-1234','O','经济舱',30),
        ('C-1234','P','经济舱',30),
        ('C-1234','Q','经济舱',30),
        ('C-1234','R','经济舱',30),
        ('C-1234','S','经济舱',30),
        ('C-1234','T','经济舱',30),
   ('C-2234','A','头等舱',10),
        ('C-2234','B','公务舱',20),
        ('C-2234','C','公务舱',20),
        ('C-2234','D','公务舱',20),
        ('C-2234','E','公务舱',20),
        ('C-2234','F','公务舱',20),
        ('C-2234','G','公务舱',20),
        ('C-2234','H','经济舱',30),
        ('C-2234','I','经济舱',30),
        ('C-2234','J','经济舱',30),
        ('C-2234','K','经济舱',30),
        ('C-2234','L','经济舱',30),
        ('C-2234','M','经济舱',30),
        ('C-2234','N','经济舱',30),
        ('C-2234','O','经济舱',30),
        ('C-2234','P','经济舱',30),
        ('C-2234','Q','经济舱',30),
        ('C-2234','R','经济舱',30),
        ('C-2234','S','经济舱',30),
        ('C-2234','T','经济舱',30),
        ('C-3234','A','头等舱',10),
        ('C-3234','B','公务舱',20),
        ('C-3234','C','公务舱',20),
        ('C-3234','D','公务舱',20),
        ('C-3234','E','公务舱',20),
        ('C-3234','F','公务舱',20),
        ('C-3234','G','公务舱',20),
        ('C-3234','H','经济舱',30),
        ('C-3234','I','经济舱',30),
        ('C-3234','J','经济舱',30),
        ('C-3234','K','经济舱',30),
        ('C-3234','L','经济舱',30),
        ('C-3234','M','经济舱',30),
        ('C-3234','N','经济舱',30),
        ('C-3234','O','经济舱',30),
        ('C-3234','P','经济舱',30),
        ('C-3234','Q','经济舱',30),
        ('C-3234','R','经济舱',30),
        ('C-3234','S','经济舱',30),
        ('C-3234','T','经济舱',30)
GO
DECLARE @Itinerary_id char(12);
EXEC [Create_Itinerary] '2021-06-16 8:00:00','2021-06-16 10:15:00','2021-06-16','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-17 8:00:00','2021-06-17 10:15:00','2021-06-17','GJ8006', 'B-6341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-18 8:00:00','2021-06-18 10:15:00','2021-06-18','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-19 8:00:00','2021-06-19 10:15:00','2021-06-19','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-20 8:00:00','2021-06-20 10:15:00','2021-06-20','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-21 8:00:00','2021-06-21 10:15:00','2021-06-21','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-22 8:00:00','2021-06-22 10:15:00','2021-06-22','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-23 8:00:00','2021-06-23 10:15:00','2021-06-23','GJ8006', 'B-6341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-24 8:00:00','2021-06-24 10:15:00','2021-06-24','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-25 8:00:00','2021-06-25 10:15:00','2021-06-25','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-26 8:00:00','2021-06-26 10:15:00','2021-06-26','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-27 8:00:00','2021-06-27 10:15:00','2021-06-27','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-28 8:00:00','2021-06-28 10:15:00','2021-06-28','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-29 8:00:00','2021-06-29 10:15:00','2021-06-29','GJ8006', 'B-6341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-30 8:00:00','2021-06-30 10:15:00','2021-06-30','GJ8006', 'B-2341',@Itinerary_id OUTPUT;
GO
DECLARE @Itinerary_id char(12);

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'GJ8006' 
AND [Plan_departuredate] = '2021-06-16'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-16 8:50:00',
    [Arrivaltime] = '2021-06-16 10:40:00',
    [Flight_status] ='航班到达',
    [Mileage] = 568
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-2341','A',6480,10),
        (@Itinerary_id,'B-2341','B',5800,20),
        (@Itinerary_id,'B-2341','C',4910,20),
        (@Itinerary_id,'B-2341','D',4380,20),
        (@Itinerary_id,'B-2341','E',3480,20),
        (@Itinerary_id,'B-2341','F',2690,30),
        (@Itinerary_id,'B-2341','H',1790,30),
        (@Itinerary_id,'B-2341','I',1760,30),
        (@Itinerary_id,'B-2341','J',1380,30),
        (@Itinerary_id,'B-2341','K',1230,30),
        (@Itinerary_id,'B-2341','L',1340,30),
        (@Itinerary_id,'B-2341','M',1160,30),
        (@Itinerary_id,'B-2341','O',950,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'GJ8006' 
AND [Plan_departuredate] = '2021-06-17'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-17 8:20:00',
    [Arrivaltime] = '2021-06-17 10:20:00',
    [Flight_status] ='航班到达',
    [Mileage] = 568
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-2341','A',6480,10),
        (@Itinerary_id,'B-2341','B',5800,20),
        (@Itinerary_id,'B-2341','C',4910,20),
        (@Itinerary_id,'B-2341','D',4380,20),
        (@Itinerary_id,'B-2341','E',3480,20),
        (@Itinerary_id,'B-2341','F',2690,30),
        (@Itinerary_id,'B-2341','H',1790,30),
        (@Itinerary_id,'B-2341','I',1760,30),
        (@Itinerary_id,'B-2341','J',1380,30),
        (@Itinerary_id,'B-2341','K',1230,30),
        (@Itinerary_id,'B-2341','L',1340,30),
        (@Itinerary_id,'B-2341','M',1160,30),
        (@Itinerary_id,'B-2341','O',950,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'GJ8006' 
AND [Plan_departuredate] = '2021-06-18'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-18 7:53:00',
    [Arrivaltime] = '2021-06-18 10:10:00',
    [Flight_status] ='航班到达',
    [Mileage] = 568
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-2341','A',6480,10),
        (@Itinerary_id,'B-2341','B',5800,20),
        (@Itinerary_id,'B-2341','C',4910,20),
        (@Itinerary_id,'B-2341','D',4380,20),
        (@Itinerary_id,'B-2341','E',3480,20),
        (@Itinerary_id,'B-2341','F',2690,30),
        (@Itinerary_id,'B-2341','H',1790,30),
        (@Itinerary_id,'B-2341','I',1760,30),
        (@Itinerary_id,'B-2341','J',1380,30),
        (@Itinerary_id,'B-2341','K',1230,30),
        (@Itinerary_id,'B-2341','L',1340,30),
        (@Itinerary_id,'B-2341','M',1160,30),
        (@Itinerary_id,'B-2341','O',950,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'GJ8006' 
AND [Plan_departuredate] = '2021-06-19'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-19 8:05:00',
    [Arrivaltime] = '2021-06-19 10:36:00',
    [Flight_status] ='航班到达',
    [Mileage] = 568
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-2341','A',6480,10),
        (@Itinerary_id,'B-2341','B',5800,20),
        (@Itinerary_id,'B-2341','C',4910,20),
        (@Itinerary_id,'B-2341','D',4380,20),
        (@Itinerary_id,'B-2341','E',3480,20),
        (@Itinerary_id,'B-2341','F',2690,30),
        (@Itinerary_id,'B-2341','H',1790,30),
        (@Itinerary_id,'B-2341','I',1760,30),
        (@Itinerary_id,'B-2341','J',1380,30),
        (@Itinerary_id,'B-2341','K',1230,30),
        (@Itinerary_id,'B-2341','L',1340,30),
        (@Itinerary_id,'B-2341','M',1160,30),
        (@Itinerary_id,'B-2341','O',950,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'GJ8006' 
AND [Plan_departuredate] = '2021-06-20'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-20 7:59:00',
    [Arrivaltime] = '2021-06-20 10:11:00',
    [Flight_status] ='航班到达',
    [Mileage] = 568
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-2341','A',6480,10),
        (@Itinerary_id,'B-2341','B',5800,20),
        (@Itinerary_id,'B-2341','C',4910,20),
        (@Itinerary_id,'B-2341','D',4380,20),
        (@Itinerary_id,'B-2341','E',3480,20),
        (@Itinerary_id,'B-2341','F',2690,30),
        (@Itinerary_id,'B-2341','H',1790,30),
        (@Itinerary_id,'B-2341','I',1760,30),
        (@Itinerary_id,'B-2341','J',1380,30),
        (@Itinerary_id,'B-2341','K',1230,30),
        (@Itinerary_id,'B-2341','L',1340,30),
        (@Itinerary_id,'B-2341','M',1160,30),
        (@Itinerary_id,'B-2341','O',950,30)
GO

DECLARE @Itinerary_id char(12);
EXEC [Create_Itinerary] '2021-06-16 10:00:00','2021-06-16 12:15:00','2021-06-16','HU7442', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-18 10:00:00','2021-06-18 12:15:00','2021-06-18','HU7442', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-20 10:00:00','2021-06-20 12:15:00','2021-06-20','HU7442', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-22 10:00:00','2021-06-22 12:15:00','2021-06-22','HU7442', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-24 10:00:00','2021-06-24 12:15:00','2021-06-24','HU7442', 'C-2234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-26 10:00:00','2021-06-26 12:15:00','2021-06-26','HU7442', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-28 10:00:00','2021-06-28 12:15:00','2021-06-28','HU7442', 'C-2234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-30 10:00:00','2021-06-30 12:15:00','2021-06-30','HU7442', 'C-1234',@Itinerary_id OUTPUT;
GO
DECLARE @Itinerary_id char(12);

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'HU7442' 
AND [Plan_departuredate] = '2021-06-16'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-16 10:21:00',
    [Arrivaltime] = '2021-06-16 12:30:00',
    [Flight_status] ='航班到达',
    [Mileage] = 255
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-1234','A',6240,10),
        (@Itinerary_id,'C-1234','B',5600,20),
        (@Itinerary_id,'C-1234','C',4510,20),
        (@Itinerary_id,'C-1234','D',4380,20),
        (@Itinerary_id,'C-1234','E',3480,20),
        (@Itinerary_id,'C-1234','F',2690,30),
        (@Itinerary_id,'C-1234','H',2390,30),
        (@Itinerary_id,'C-1234','I',1930,30),
        (@Itinerary_id,'C-1234','J',1680,30),
        (@Itinerary_id,'C-1234','K',1530,30),
        (@Itinerary_id,'C-1234','L',1240,30),
        (@Itinerary_id,'C-1234','M',1060,30),
        (@Itinerary_id,'C-1234','O',750,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'HU7442' 
AND [Plan_departuredate] = '2021-06-18'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-18 10:06:00',
    [Arrivaltime] = '2021-06-18 12:40:00',
    [Flight_status] ='航班到达',
    [Mileage] = 255
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-1234','A',6240,10),
        (@Itinerary_id,'C-1234','B',5600,20),
        (@Itinerary_id,'C-1234','C',4510,20),
        (@Itinerary_id,'C-1234','D',4380,20),
        (@Itinerary_id,'C-1234','E',3480,20),
        (@Itinerary_id,'C-1234','F',2690,30),
        (@Itinerary_id,'C-1234','H',2390,30),
        (@Itinerary_id,'C-1234','I',1930,30),
        (@Itinerary_id,'C-1234','J',1680,30),
        (@Itinerary_id,'C-1234','K',1530,30),
        (@Itinerary_id,'C-1234','L',1240,30),
        (@Itinerary_id,'C-1234','M',1060,30),
        (@Itinerary_id,'C-1234','O',750,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'HU7442' 
AND [Plan_departuredate] = '2021-06-20'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-20 9:50:00',
    [Arrivaltime] = '2021-06-20 12:02:00',
    [Flight_status] ='航班到达',
    [Mileage] = 255
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-1234','A',6240,10),
        (@Itinerary_id,'C-1234','B',5600,20),
        (@Itinerary_id,'C-1234','C',4510,20),
        (@Itinerary_id,'C-1234','D',4380,20),
        (@Itinerary_id,'C-1234','E',3480,20),
        (@Itinerary_id,'C-1234','F',2690,30),
        (@Itinerary_id,'C-1234','H',2390,30),
        (@Itinerary_id,'C-1234','I',1930,30),
        (@Itinerary_id,'C-1234','J',1680,30),
        (@Itinerary_id,'C-1234','K',1530,30),
        (@Itinerary_id,'C-1234','L',1240,30),
        (@Itinerary_id,'C-1234','M',1060,30),
        (@Itinerary_id,'C-1234','O',750,30)
GO

DECLARE @Itinerary_id char(12);
EXEC [Create_Itinerary] '2021-06-16 15:00:00','2021-06-16 18:15:00','2021-06-16','HO1243', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-17 15:00:00','2021-06-17 18:15:00','2021-06-17','HO1243', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-18 15:00:00','2021-06-18 18:15:00','2021-06-18','HO1243', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-19 15:00:00','2021-06-19 18:15:00','2021-06-19','HO1243', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-20 15:00:00','2021-06-20 18:15:00','2021-06-20','HO1243', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-22 15:00:00','2021-06-22 18:15:00','2021-06-22','HO1243', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-24 15:00:00','2021-06-24 18:15:00','2021-06-24','HO1243', 'C-2234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-26 15:00:00','2021-06-26 18:15:00','2021-06-26','HO1243', 'C-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-28 15:00:00','2021-06-28 18:15:00','2021-06-28','HO1243', 'C-2234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-30 15:00:00','2021-06-30 18:15:00','2021-06-30','HO1243', 'C-1234',@Itinerary_id OUTPUT;
GO
DECLARE @Itinerary_id char(12);

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'HO1243' 
AND [Plan_departuredate] = '2021-06-16'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-16 15:21:00',
    [Arrivaltime] = '2021-06-16 18:30:00',
    [Flight_status] ='航班到达',
    [Mileage] = 795
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-1234','A',4340,10),
        (@Itinerary_id,'C-1234','B',4100,20),
        (@Itinerary_id,'C-1234','C',4010,20),
        (@Itinerary_id,'C-1234','D',3880,20),
        (@Itinerary_id,'C-1234','E',3480,20),
        (@Itinerary_id,'C-1234','F',2390,30),
        (@Itinerary_id,'C-1234','H',2190,30),
        (@Itinerary_id,'C-1234','I',1730,30),
        (@Itinerary_id,'C-1234','J',1680,30),
        (@Itinerary_id,'C-1234','K',1530,30),
        (@Itinerary_id,'C-1234','L',1140,30),
        (@Itinerary_id,'C-1234','M',960,30),
        (@Itinerary_id,'C-1234','O',850,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'HO1243' 
AND [Plan_departuredate] = '2021-06-17'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-17 14:49:00',
    [Arrivaltime] = '2021-06-17 18:04:00',
    [Flight_status] ='航班到达',
    [Mileage] = 795
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-1234','A',4340,10),
        (@Itinerary_id,'C-1234','B',4100,20),
        (@Itinerary_id,'C-1234','C',4010,20),
        (@Itinerary_id,'C-1234','D',3880,20),
        (@Itinerary_id,'C-1234','E',3480,20),
        (@Itinerary_id,'C-1234','F',2390,30),
        (@Itinerary_id,'C-1234','H',2190,30),
        (@Itinerary_id,'C-1234','I',1730,30),
        (@Itinerary_id,'C-1234','J',1680,30),
        (@Itinerary_id,'C-1234','K',1530,30),
        (@Itinerary_id,'C-1234','L',1140,30),
        (@Itinerary_id,'C-1234','M',960,30),
        (@Itinerary_id,'C-1234','O',850,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'HO1243' 
AND [Plan_departuredate] = '2021-06-18'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-18 15:04:00',
    [Arrivaltime] = '2021-06-18 18:35:00',
    [Flight_status] ='航班到达',
    [Mileage] = 795
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-1234','A',4340,10),
        (@Itinerary_id,'C-1234','B',4100,20),
        (@Itinerary_id,'C-1234','C',4010,20),
        (@Itinerary_id,'C-1234','D',3880,20),
        (@Itinerary_id,'C-1234','E',3480,20),
        (@Itinerary_id,'C-1234','F',2390,30),
        (@Itinerary_id,'C-1234','H',2190,30),
        (@Itinerary_id,'C-1234','I',1730,30),
        (@Itinerary_id,'C-1234','J',1680,30),
        (@Itinerary_id,'C-1234','K',1530,30),
        (@Itinerary_id,'C-1234','L',1140,30),
        (@Itinerary_id,'C-1234','M',960,30),
        (@Itinerary_id,'C-1234','O',850,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'HO1243' 
AND [Plan_departuredate] = '2021-06-19'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-19 14:59:00',
    [Arrivaltime] = '2021-06-19 18:18:00',
    [Flight_status] ='航班到达',
    [Mileage] = 795
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-1234','A',4340,10),
        (@Itinerary_id,'C-1234','B',4100,20),
        (@Itinerary_id,'C-1234','C',4010,20),
        (@Itinerary_id,'C-1234','D',3880,20),
        (@Itinerary_id,'C-1234','E',3480,20),
        (@Itinerary_id,'C-1234','F',2390,30),
        (@Itinerary_id,'C-1234','H',2190,30),
        (@Itinerary_id,'C-1234','I',1730,30),
        (@Itinerary_id,'C-1234','J',1680,30),
        (@Itinerary_id,'C-1234','K',1530,30),
        (@Itinerary_id,'C-1234','L',1140,30),
        (@Itinerary_id,'C-1234','M',960,30),
        (@Itinerary_id,'C-1234','O',850,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'HO1243' 
AND [Plan_departuredate] = '2021-06-20'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-20 14:49:00',
    [Arrivaltime] = '2021-06-20 17:53:00',
    [Flight_status] ='航班到达',
    [Mileage] = 795
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-1234','A',4340,10),
        (@Itinerary_id,'C-1234','B',4100,20),
        (@Itinerary_id,'C-1234','C',4010,20),
        (@Itinerary_id,'C-1234','D',3880,20),
        (@Itinerary_id,'C-1234','E',3480,20),
        (@Itinerary_id,'C-1234','F',2390,30),
        (@Itinerary_id,'C-1234','H',2190,30),
        (@Itinerary_id,'C-1234','I',1730,30),
        (@Itinerary_id,'C-1234','J',1680,30),
        (@Itinerary_id,'C-1234','K',1530,30),
        (@Itinerary_id,'C-1234','L',1140,30),
        (@Itinerary_id,'C-1234','M',960,30),
        (@Itinerary_id,'C-1234','O',850,30)
GO

DECLARE @Itinerary_id char(12);
EXEC [Create_Itinerary] '2021-06-16 5:00:00','2021-06-16 8:30:00','2021-06-16','G54874', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-17 5:00:00','2021-06-17 8:30:00','2021-06-17','G54874', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-18 5:00:00','2021-06-18 8:30:00','2021-06-18','G54874', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-19 5:00:00','2021-06-19 8:30:00','2021-06-19','G54874', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-20 5:00:00','2021-06-20 8:30:00','2021-06-20','G54874', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-22 5:00:00','2021-06-22 8:30:00','2021-06-22','G54874', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-24 5:00:00','2021-06-24 8:30:00','2021-06-24','G54874', 'B-1234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-26 5:00:00','2021-06-26 8:30:00','2021-06-26','G54874', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-28 5:00:00','2021-06-28 8:30:00','2021-06-28','G54874', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-30 5:00:00','2021-06-30 8:30:00','2021-06-30','G54874', 'B-1234',@Itinerary_id OUTPUT;
GO
DECLARE @Itinerary_id char(12);

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'G54874' 
AND [Plan_departuredate] = '2021-06-16'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-16 4:49:00',
    [Arrivaltime] = '2021-06-16 8:58:00',
    [Flight_status] ='航班到达',
    [Mileage] = 358
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-2341','A',6480,10),
        (@Itinerary_id,'B-2341','B',5800,20),
        (@Itinerary_id,'B-2341','C',4910,20),
        (@Itinerary_id,'B-2341','D',4380,20),
        (@Itinerary_id,'B-2341','E',3480,20),
        (@Itinerary_id,'B-2341','F',2690,30),
        (@Itinerary_id,'B-2341','H',1790,30),
        (@Itinerary_id,'B-2341','I',1760,30),
        (@Itinerary_id,'B-2341','J',1380,30),
        (@Itinerary_id,'B-2341','K',1230,30),
        (@Itinerary_id,'B-2341','L',1340,30),
        (@Itinerary_id,'B-2341','M',1160,30),
        (@Itinerary_id,'B-2341','O',950,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'G54874' 
AND [Plan_departuredate] = '2021-06-17'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-17 5:28:00',
    [Arrivaltime] = '2021-06-17 8:59:00',
    [Flight_status] ='航班到达',
    [Mileage] = 358
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-2341','A',6480,10),
        (@Itinerary_id,'B-2341','B',5800,20),
        (@Itinerary_id,'B-2341','C',4910,20),
        (@Itinerary_id,'B-2341','D',4380,20),
        (@Itinerary_id,'B-2341','E',3480,20),
        (@Itinerary_id,'B-2341','F',2690,30),
        (@Itinerary_id,'B-2341','H',1790,30),
        (@Itinerary_id,'B-2341','I',1760,30),
        (@Itinerary_id,'B-2341','J',1380,30),
        (@Itinerary_id,'B-2341','K',1230,30),
        (@Itinerary_id,'B-2341','L',1340,30),
        (@Itinerary_id,'B-2341','M',1160,30),
        (@Itinerary_id,'B-2341','O',950,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'G54874' 
AND [Plan_departuredate] = '2021-06-19'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-19 4:58:00',
    [Arrivaltime] = '2021-06-19 8:37:00',
    [Flight_status] ='航班到达',
    [Mileage] = 358
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-2341','A',6480,10),
        (@Itinerary_id,'B-2341','B',5800,20),
        (@Itinerary_id,'B-2341','C',4910,20),
        (@Itinerary_id,'B-2341','D',4380,20),
        (@Itinerary_id,'B-2341','E',3480,20),
        (@Itinerary_id,'B-2341','F',2690,30),
        (@Itinerary_id,'B-2341','H',1790,30),
        (@Itinerary_id,'B-2341','I',1760,30),
        (@Itinerary_id,'B-2341','J',1380,30),
        (@Itinerary_id,'B-2341','K',1230,30),
        (@Itinerary_id,'B-2341','L',1340,30),
        (@Itinerary_id,'B-2341','M',1160,30),
        (@Itinerary_id,'B-2341','O',950,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'G54874' 
AND [Plan_departuredate] = '2021-06-20'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-20 5:04:00',
    [Arrivaltime] = '2021-06-20 8:14:00',
    [Flight_status] ='航班到达',
    [Mileage] = 358
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'B-2341','A',6480,10),
        (@Itinerary_id,'B-2341','B',5800,20),
        (@Itinerary_id,'B-2341','C',4910,20),
        (@Itinerary_id,'B-2341','D',4380,20),
        (@Itinerary_id,'B-2341','E',3480,20),
        (@Itinerary_id,'B-2341','F',2690,30),
        (@Itinerary_id,'B-2341','H',1790,30),
        (@Itinerary_id,'B-2341','I',1760,30),
        (@Itinerary_id,'B-2341','J',1380,30),
        (@Itinerary_id,'B-2341','K',1230,30),
        (@Itinerary_id,'B-2341','L',1340,30),
        (@Itinerary_id,'B-2341','M',1160,30),
        (@Itinerary_id,'B-2341','O',950,30)
GO

DECLARE @Itinerary_id char(12);
EXEC [Create_Itinerary] '2021-06-16 11:00:00','2021-06-16 13:00:00','2021-06-16','CZ9541', 'C-3234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-19 11:00:00','2021-06-19 13:00:00','2021-06-17','CZ9541', 'C-3234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-22 11:00:00','2021-06-22 13:00:00','2021-06-18','CZ9541', 'C-2234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-25 11:00:00','2021-06-25 13:00:00','2021-06-19','CZ9541', 'C-3234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-28 11:00:00','2021-06-28 13:00:00','2021-06-20','CZ9541', 'C-2234',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-30 11:00:00','2021-06-30 13:00:00','2021-06-30','CZ9541', 'C-3234',@Itinerary_id OUTPUT;
GO
DECLARE @Itinerary_id char(12);

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'CZ9541' 
AND [Plan_departuredate] = '2021-06-16'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-16 11:04:00',
    [Arrivaltime] = '2021-06-16 13:24:00',
    [Flight_status] ='航班到达',
    [Mileage] = 922
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-3234','A',8480,10),
        (@Itinerary_id,'C-3234','B',7800,20),
        (@Itinerary_id,'C-3234','C',6910,20),
        (@Itinerary_id,'C-3234','D',5380,20),
        (@Itinerary_id,'C-3234','E',4480,20),
        (@Itinerary_id,'C-3234','F',3690,30),
        (@Itinerary_id,'C-3234','H',2790,30),
        (@Itinerary_id,'C-3234','I',1760,30),
        (@Itinerary_id,'C-3234','J',1380,30),
        (@Itinerary_id,'C-3234','K',1130,30),
        (@Itinerary_id,'C-3234','L',1240,30),
        (@Itinerary_id,'C-3234','M',960,30),
        (@Itinerary_id,'C-3234','O',550,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'CZ9541' 
AND [Plan_departuredate] = '2021-06-19'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-19 11:44:00',
    [Arrivaltime] = '2021-06-19 13:54:00',
    [Flight_status] ='航班到达',
    [Mileage] = 922
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-3234','A',8480,10),
        (@Itinerary_id,'C-3234','B',7800,20),
        (@Itinerary_id,'C-3234','C',6910,20),
        (@Itinerary_id,'C-3234','D',5380,20),
        (@Itinerary_id,'C-3234','E',4480,20),
        (@Itinerary_id,'C-3234','F',3690,30),
        (@Itinerary_id,'C-3234','H',2790,30),
        (@Itinerary_id,'C-3234','I',1760,30),
        (@Itinerary_id,'C-3234','J',1380,30),
        (@Itinerary_id,'C-3234','K',1130,30),
        (@Itinerary_id,'C-3234','L',1240,30),
        (@Itinerary_id,'C-3234','M',960,30),
        (@Itinerary_id,'C-3234','O',550,30)
GO

DECLARE @Itinerary_id char(12);
EXEC [Create_Itinerary] '2021-06-16 1:00:00','2021-06-16 5:15:00','2021-06-16','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-17 1:00:00','2021-06-17 5:15:00','2021-06-17','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-18 1:00:00','2021-06-18 5:15:00','2021-06-18','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-19 1:00:00','2021-06-19 5:15:00','2021-06-19','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-20 1:00:00','2021-06-20 5:15:00','2021-06-20','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-21 1:00:00','2021-06-21 5:15:00','2021-06-21','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-22 1:00:00','2021-06-22 5:15:00','2021-06-22','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-23 1:00:00','2021-06-23 5:15:00','2021-06-23','JD5175', 'B-6341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-24 1:00:00','2021-06-24 5:15:00','2021-06-24','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-25 1:00:00','2021-06-25 5:15:00','2021-06-25','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-26 1:00:00','2021-06-26 5:15:00','2021-06-26','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-27 1:00:00','2021-06-27 5:15:00','2021-06-27','JD5175', 'B-6341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-28 1:00:00','2021-06-28 5:15:00','2021-06-28','JD5175', 'B-2341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-29 1:00:00','2021-06-29 5:15:00','2021-06-29','JD5175', 'B-6341',@Itinerary_id OUTPUT;
EXEC [Create_Itinerary] '2021-06-30 1:00:00','2021-06-30 5:15:00','2021-06-30','JD5175', 'B-2341',@Itinerary_id OUTPUT;
GO
DECLARE @Itinerary_id char(12);

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'JD5175' 
AND [Plan_departuredate] = '2021-06-16'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-16 1:44:00',
    [Arrivaltime] = '2021-06-16 5:54:00',
    [Flight_status] ='航班到达',
    [Mileage] = 834
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-3234','A',6480,10),
        (@Itinerary_id,'C-3234','B',5800,20),
        (@Itinerary_id,'C-3234','C',4910,20),
        (@Itinerary_id,'C-3234','D',4380,20),
        (@Itinerary_id,'C-3234','E',4480,20),
        (@Itinerary_id,'C-3234','F',3890,30),
        (@Itinerary_id,'C-3234','H',2690,30),
        (@Itinerary_id,'C-3234','I',1960,30),
        (@Itinerary_id,'C-3234','J',1850,30),
        (@Itinerary_id,'C-3234','K',1640,30),
        (@Itinerary_id,'C-3234','L',1320,30),
        (@Itinerary_id,'C-3234','M',910,30),
        (@Itinerary_id,'C-3234','O',700,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'JD5175' 
AND [Plan_departuredate] = '2021-06-17'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-17 1:34:00',
    [Arrivaltime] = '2021-06-17 4:56:00',
    [Flight_status] ='航班到达',
    [Mileage] = 834
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-3234','A',6480,10),
        (@Itinerary_id,'C-3234','B',5800,20),
        (@Itinerary_id,'C-3234','C',4910,20),
        (@Itinerary_id,'C-3234','D',4380,20),
        (@Itinerary_id,'C-3234','E',4480,20),
        (@Itinerary_id,'C-3234','F',3890,30),
        (@Itinerary_id,'C-3234','H',2690,30),
        (@Itinerary_id,'C-3234','I',1960,30),
        (@Itinerary_id,'C-3234','J',1850,30),
        (@Itinerary_id,'C-3234','K',1640,30),
        (@Itinerary_id,'C-3234','L',1320,30),
        (@Itinerary_id,'C-3234','M',910,30),
        (@Itinerary_id,'C-3234','O',700,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'JD5175' 
AND [Plan_departuredate] = '2021-06-18'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-18 1:03:00',
    [Arrivaltime] = '2021-06-18 5:21:00',
    [Flight_status] ='航班到达',
    [Mileage] = 834
WHERE @Itinerary_id = [Itinerary_id]; 

INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-3234','A',6480,10),
        (@Itinerary_id,'C-3234','B',5800,20),
        (@Itinerary_id,'C-3234','C',4910,20),
        (@Itinerary_id,'C-3234','D',4380,20),
        (@Itinerary_id,'C-3234','E',4480,20),
        (@Itinerary_id,'C-3234','F',3890,30),
        (@Itinerary_id,'C-3234','H',2690,30),
        (@Itinerary_id,'C-3234','I',1960,30),
        (@Itinerary_id,'C-3234','J',1850,30),
        (@Itinerary_id,'C-3234','K',1640,30),
        (@Itinerary_id,'C-3234','L',1320,30),
        (@Itinerary_id,'C-3234','M',910,30),
        (@Itinerary_id,'C-3234','O',700,30)

SELECT @Itinerary_id = [Itinerary_id]
FROM [Itinerary]
WHERE [Flight_NO] = 'JD5175' 
AND [Plan_departuredate] = '2021-06-20'; 

UPDATE [Itinerary]
SET [Departuretime] = '2021-06-20 1:12:00',
    [Arrivaltime] = '2021-06-20 4:49:00',
    [Flight_status] ='航班到达',
    [Mileage] = 834
WHERE @Itinerary_id = [Itinerary_id]; 


INSERT INTO [Itinerary_Cabin]
VALUES  (@Itinerary_id,'C-3234','A',6480,10),
        (@Itinerary_id,'C-3234','B',5800,20),
        (@Itinerary_id,'C-3234','C',4910,20),
        (@Itinerary_id,'C-3234','D',4380,20),
        (@Itinerary_id,'C-3234','E',4480,20),
        (@Itinerary_id,'C-3234','F',3890,30),
        (@Itinerary_id,'C-3234','H',2690,30),
        (@Itinerary_id,'C-3234','I',1960,30),
        (@Itinerary_id,'C-3234','J',1850,30),
        (@Itinerary_id,'C-3234','K',1640,30),
        (@Itinerary_id,'C-3234','L',1320,30),
        (@Itinerary_id,'C-3234','M',910,30),
        (@Itinerary_id,'C-3234','O',700,30)