USE Ticket_reservation --机票信息 
GO 
--航班动态
CREATE VIEW [Flights]
AS
SELECT  [I].[Flight_NO] AS '航班号',
        [Plan_departuredate],
        [Plan_departuretime],
        [Plan_arrivaltime],
        [Airline],
        [a1].[City] AS '出发城市',
        [a1].[Airport_name] AS '出发机场名',
        [Departure_teminal],
        [a2].[City] AS '到达城市',
        [a2].[Airport_name] AS '到达机场名',
        [Arrival_teminal],
        [Departuretime],
        [Arrivaltime],
        [Flight_status],
        [Mileage],
        ABS(DATEDIFF(mi,[Arrivaltime],[Departuretime])) AS '飞行时长',
        [Itinerary_id]
FROM [dbo].[Itinerary] [I]
JOIN [dbo].[Flight] [F]
ON [I].[Flight_NO]=[F].[Flight_NO]
JOIN [dbo].[Airport] [a1]
ON [F].[Departure_apcode]=[a1].[Airport_code]
JOIN [dbo].[Airport] [a2]
ON [F].[Arrival_apcode]=[a2].[Airport_code]
WHERE DATEDIFF(d,[Plan_departuredate],GETDATE()) < 5
GO
-- 出发延误时间和次数
CREATE VIEW [Delay_Departuretime]
AS
SELECT [Flight_NO],
       AVG(CONVERT(int,DATEDIFF(n,[Plan_departuretime],[Departuretime]))) AS '出发平均延误时间',
       COUNT([itinerary].[Itinerary_id]) AS '出发延误次数'
FROM [dbo].[Itinerary]
WHERE DATEDIFF(n,[Plan_departuretime],[Departuretime]) > 15 AND [Flight_status]='航班到达'
GROUP BY [Flight_NO]
GO
-- 降落延误时间和次数
CREATE VIEW [Delay_Arrivaltime]
AS
SELECT [Flight_NO],
       AVG(CONVERT(int,DATEDIFF(n,[Plan_arrivaltime],[Arrivaltime]))) AS '降落平均延误时间',
       COUNT([itinerary].[Itinerary_id]) AS '降落延误次数'
FROM [dbo].[Itinerary]
WHERE DATEDIFF(n,[Plan_arrivaltime],[Arrivaltime]) > 15 AND [Flight_status]='航班到达'
GROUP BY [Flight_NO]
GO
-- 航班详情(出发降落准点率及平均延误时间)
CREATE VIEW [Flight_Detail]
AS
SELECT [I].[Flight_NO] AS '航班号',
       100-100*[出发延误次数]/COUNT([I].[Itinerary_id]) AS '出发准点率',
       100-100*[降落延误次数]/COUNT([I].[Itinerary_id]) AS '降落准点率',
       [出发平均延误时间],
       [降落平均延误时间]
FROM [dbo].[Itinerary] [I]
JOIN [dbo].[Delay_Departuretime] [DD]
ON [I].[Flight_NO] = [DD].[Flight_NO]
JOIN [dbo].[Delay_Arrivaltime] [DA]
ON [I].[Flight_NO] = [DA].[Flight_NO]
WHERE [Flight_status]='航班到达'
GROUP BY [I].[Flight_NO],[出发平均延误时间],[降落平均延误时间],[出发延误次数],[降落延误次数]

GO
-- 机票详情
Create VIEW [Ticket]
As 
SELECT [F].[Flight_NO] AS '航班号1',
       [Plane_model],
       [Airline],
       [Plan_departuredate],
       [Plan_departuretime],
       [Plan_arrivaltime],
       [a1].[City] AS '出发城市',
       [a1].[Airport_name] AS '起飞机场名',
       [Departure_teminal],
       [a2].[City] AS '到达城市',
       [a2].[Airport_name] AS '到达机场名',
       [Arrival_teminal],
       [Cabin_type],
       [Price],
       [出发准点率],
       [I].[Itinerary_id] AS '行程号',
       [IC].[Plane_NO] AS '飞机号',
       [IC].[Cabin_code] AS '舱位代码'
FROM [dbo].[Itinerary] [I]
JOIN [dbo].[Flight] [F]
ON [I].[Flight_NO]=[F].[Flight_NO]
JOIN [dbo].[Airplane] [A]
ON [I].[Plane_NO]= [A].[Plane_NO]
JOIN [dbo].[Itinerary_Cabin] [IC]
ON [IC].[Itinerary_id]=[I].[Itinerary_id]
JOIN [dbo].[Cabin]
ON [IC].[Plane_NO]=[Cabin].[Plane_NO] AND [IC].[Cabin_code]=[Cabin].[Cabin_code]
JOIN [dbo].[Airport] [a1]
ON [F].[Departure_apcode]=[a1].[Airport_code]
JOIN [dbo].[Airport] [a2]
ON [F].[Arrival_apcode]=[a2].[Airport_code]
JOIN [dbo].[Flight_Detail] [FD]
ON [FD].[航班号]=[I].[Flight_NO]
WHERE DATEDIFF(hh,GETDATE(),[Plan_departuretime]) > 1
GO
-- 订单详情
CREATE VIEW [Order_Detail]
AS
SELECT [Order_id],
       [Order_pay],
       [Contact_Phone],
       [Order_status],
       [Plan_departuredate],
       [Plan_departuretime],
       [Plan_arrivaltime],
       [Airline],
       [a1].[City] AS '出发城市',
       [a1].[Airport_name] AS '起飞机场名',
       [Departure_teminal],
       [a2].[City] AS '到达城市',
       [a2].[Airport_name] AS '达到机场名',
        [Arrival_teminal],
       [Order].[Itinerary_id] AS '航班号',
       [Cabin_type]
FROM [Order]
JOIN [Itinerary]
ON [Order].[Itinerary_id]=[Itinerary].[Itinerary_id]
JOIN [Flight]
ON [Itinerary].[Flight_NO]=[Flight].[Flight_NO]
JOIN [Cabin]
ON [Order].[Plane_NO]=[Cabin].[Plane_NO] AND [Order].[Cabin_code]=[Cabin].[Cabin_code]
JOIN [Airport] [a1]
ON [Flight].[Departure_apcode]=[a1].[Airport_code]
JOIN [Airport] [a2]
ON [Flight].[Arrival_apcode]=[a2].[Airport_code]
GO

