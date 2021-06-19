CREATE DATABASE Ticket_reservation
GO
USE Ticket_reservation
GO
-- 用户
CREATE TABLE [User] (
	[Uname] varchar(20) NOT NULL, 	-- 用户名
	[Passwd] varchar(20) NOT NULL,	-- 密码
	[Phone] char(11),				-- 手机号
	[Sex] char(2) DEFAULT '男',		-- 性别
	[Name] varchar(30),				-- 姓名
	[Email] varchar(320),			-- 邮箱
	PRIMARY KEY ([Uname]),
	CHECK ([Sex] IN ('男', '女'))
)
GO
-- 机场
CREATE TABLE [Airport] (
	[Airport_code] char(4) NOT NULL,		-- 机场代码
	[City] varchar(100) NOT NULL,			-- 城市
	[Airport_name] varchar(100) NOT NULL,	-- 机场名
	PRIMARY KEY ([Airport_code])
)
GO
-- 航班
CREATE TABLE [Flight] (
	[Flight_NO] char(6) NOT NULL,			-- 航班号
	[Departure_apcode] char(4) NOT NULL,	-- 出发机场代码
	[Arrival_apcode] char(4) NOT NULL,		-- 到达机场代码
	[Departure_teminal] char(2) NOT NULL,	-- 出发航站楼
	[Arrival_teminal] char(2) NOT NULL,		-- 到达航站楼
	[Airline] varchar(100) NOT NULL,		-- 航空公司
	PRIMARY KEY ([Flight_NO]),
	FOREIGN KEY ([Departure_apcode])
		REFERENCES [Airport] ([Airport_code]),
	FOREIGN KEY ([Arrival_apcode])
		REFERENCES [Airport] ([Airport_code])
)
GO
-- 飞机
CREATE TABLE [Airplane] (
	[Plane_NO] char(10) NOT NULL,		-- 飞机号
	[Plane_model] varchar(20) NOT NULL,	-- 机型
	[Plane_type] char(4) NOT NULL,		-- 类型
	PRIMARY KEY ([Plane_NO]),
	CHECK ([Plane_type] IN ('窄体', '宽体'))
)
GO
-- 行程
CREATE TABLE [Itinerary] (
	[Itinerary_id] char(12) NOT NULL,		-- 行程号
	[Plan_departuretime] datetime NOT NULL,		-- 计划起飞时间
	[Plan_arrivaltime] datetime NOT NULL,		-- 计划到达时间
	[Plan_departuredate] date NOT NULL,		-- 计划起飞日期
	[Flight_NO] char(6) NOT NULL,			-- 航班号
    [Plane_NO] char(10) NOT NULL,		-- 飞机号
	[Departuretime] datetime NOT NULL,	-- 预计/实际起飞时间
	[Arrivaltime] datetime NOT NULL,	-- 预计/实际降落时间
	[Flight_status] char(8) NOT NULL,	-- 航班状态
	[Mileage] smallint,					-- 飞行里程
	PRIMARY KEY ([Itinerary_id]),
	FOREIGN KEY ([Flight_NO])
		REFERENCES [Flight] ([Flight_NO]),
    FOREIGN KEY ([Plane_NO])
		REFERENCES [Airplane] ([Plane_NO]),
	CHECK ([Flight_status] IN (
			'航班计划', 
			'航班起飞', 
			'航班到达', 
			'航班取消', 
			'正在登机', 
			'登机结束', 
			'航班延误'
		)),
	UNIQUE ([Plan_departuredate], [Flight_NO]) -- 同一航班一天只出现一次
)

GO
-- 舱位(弱实体集依赖飞机)
CREATE TABLE [Cabin] (
	[Plane_NO] char(10) NOT NULL,		-- 飞机号
	[Cabin_code] char(1) NOT NULL,		-- 舱位代码
	[Cabin_type] char(6) NOT NULL,		-- 舱位类型
	[Seat_capacity] smallint NOT NULL,	-- 座位容量
	PRIMARY KEY ([Plane_NO], [Cabin_code]),
	FOREIGN KEY ([Plane_NO])
		REFERENCES [Airplane] ([Plane_NO])
		ON DELETE CASCADE,
	CHECK ([Cabin_type] IN ('经济舱', '公务舱', '头等舱'))
)
GO
-- 出行人(弱实体集依赖用户)
CREATE TABLE [Passenger] (
	[Uname] varchar(20) NOT NULL,	-- 用户名
	[IDCard_NO] char(18) NOT NULL,	-- 身份证号
	[Pname] varchar(30) NOT NULL,	-- 姓名
	PRIMARY KEY ([Uname], [IDCard_NO]),
	FOREIGN KEY ([Uname])
		REFERENCES [User] ([Uname])
		ON DELETE CASCADE
)
GO
-- 行程-舱位(机票)
CREATE TABLE [Itinerary_Cabin] (
	[Itinerary_id] char(12) NOT NULL,	-- 行程号
	[Plane_NO] char(10) NOT NULL,		-- 飞机号
	[Cabin_code] char(1) NOT NULL,		-- 舱位代码
	[Price] int NOT NULL,				-- 价格
	[remaining] int NOT NULL,			-- 座位余量
	PRIMARY KEY ([Itinerary_id], [Plane_NO], [Cabin_code]),
	FOREIGN KEY ([Plane_NO], [Cabin_code])
		REFERENCES [Cabin] ([Plane_NO], [Cabin_code]),
	FOREIGN KEY ([Itinerary_id])
		REFERENCES [Itinerary] ([Itinerary_id])
)
GO
-- 订单
CREATE TABLE [Order] (
	[Order_id] char(12) NOT NULL,		-- 订单号
	[Order_pay] int NOT NULL,			-- 下单金额
    [Ticker_num] smallint NOT NULL,     -- 订票数
	[Contact_Phone] char(11) NOT NULL,	-- 联系人电话
	[Itinerary_id] char(12) NOT NULL,	-- 行程号
    [Plane_NO] char(10) NOT NULL,		-- 飞机号
	[Cabin_code] char(1) NOT NULL,		-- 舱位代码
	[Uname] varchar(20) NOT NULL,		-- 用户名
	[Order_time] datetime NOT NULL,		-- 订单创建/修改时间
	[Order_status] char(10) NOT NULL,	-- 订单状态
	PRIMARY KEY ([Order_id]),
	FOREIGN KEY ([Itinerary_id],[Plane_NO],[Cabin_code])
		REFERENCES [Itinerary_Cabin]([Itinerary_id],[Plane_NO],[Cabin_code]),
	FOREIGN KEY ([Uname])
		REFERENCES [User] ([Uname])
)
GO
-- 订单-出行人
CREATE TABLE [Order_Passenger] (
	[Uname] varchar(20) NOT NULL,	-- 用户名
	[IDCard_NO] char(18) NOT NULL,	-- 身份证号
	[Order_id] char(12) NOT NULL,	-- 订单号
	[Ticket_NO] char(13) NOT NULL,	-- 票号
	PRIMARY KEY ([Uname], [IDCard_NO], [Order_id]),
	FOREIGN KEY ([Uname], [IDCard_NO])
		REFERENCES [Passenger] ([Uname], [IDCard_NO]),
	FOREIGN KEY ([Order_id])
		REFERENCES [Order] ([Order_id])
)
GO
CREATE TYPE [People] AS TABLE(
	        [IDCard_NO] char(18) NOT NULL,  -- 身份证号
	        [Pname] varchar(30) NOT NULL,	-- 姓名
            PRIMARY KEY ([IDCard_NO])
	        )
GO
CREATE INDEX [IX_Flight_Departure] 
ON [Flight]([Departure_apcode]);
GO
CREATE INDEX [IX_Flight_Arrival] 
ON [Flight]([Arrival_apcode]);
GO
CREATE INDEX [IX_Itinerary_Flight]
ON [Itinerary]([Flight_NO]);