-- Create SHIPPER table
CREATE TABLE SHIPPER (
    ShipperID INT PRIMARY KEY,
    VehicleCapacity INT,
    Area VARCHAR(255),
    Status VARCHAR(255),
    SAddress VARCHAR(255),
    SFName VARCHAR(255),
    SLName VARCHAR(255)
);

-- Create SHIPPER_PHONE_NO table
CREATE TABLE SHIPPER_PHONE_NO (
    ShipperID INT,
    PhoneNo VARCHAR(15),
    PRIMARY KEY (ShipperID, PhoneNo),
    FOREIGN KEY (ShipperID) REFERENCES SHIPPER(ShipperID)
);

-- Create AREASHIP table
CREATE TABLE AREASHIP (
    ShipperID INT,
    Area VARCHAR(255),
    PRIMARY KEY (ShipperID, Area),
    FOREIGN KEY (ShipperID) REFERENCES SHIPPER(ShipperID)
);

-- Create TAKINGORDERING table
CREATE TABLE TAKINGORDERING (
    TransactionID INT PRIMARY KEY,
    ShipperID INT,
    FOREIGN KEY (ShipperID) REFERENCES SHIPPER(ShipperID)
);

-- Create CUSTOMER table
CREATE TABLE CUSTOMER (
    CustomerID INT PRIMARY KEY,
    CAddress VARCHAR(255),
    CFName VARCHAR(255),
    CLName VARCHAR(255),
    CPhone VARCHAR(15)
);

-- Create BILL table
CREATE TABLE BILL (
    TransactionID INT PRIMARY KEY,
    PaymentMethod VARCHAR(255),
    DateAndTime DATETIME,
    CustomerID INT,
    CashierID INT,
    StoreID INT,
    FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID),
    FOREIGN KEY (CashierID) REFERENCES CASHIER(EmployeeID),
    FOREIGN KEY (StoreID) REFERENCES STORE(StoreID)
);

-- Create BILL_PROMOTION table
CREATE TABLE BILL_PROMOTION (
    ApplyPrice INT,
    PromotionID INT,
    PRIMARY KEY (ApplyPrice, PromotionID)
);

-- Create PRODUCT_PROMOTION table
CREATE TABLE PRODUCT_PROMOTION (
    PromotionID INT PRIMARY KEY
);

-- Create PROMOTEBILL table
CREATE TABLE PROMOTEBILL (
    PromotionID INT,
    TransactionID INT,
    PRIMARY KEY (PromotionID, TransactionID)
);

-- Create PROMOTEPRODUCT table
CREATE TABLE PROMOTEPRODUCT (
    PromotionID INT,
    ProductID INT,
    PRIMARY KEY (PromotionID, ProductID)
);

-- Create EMPLOYEE table
CREATE TABLE EMPLOYEE (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    Salary DECIMAL(10, 2),
    LastName VARCHAR(255),
    Address VARCHAR(255),
    StoreID INT,
    FOREIGN KEY (StoreID) REFERENCES STORE(StoreID)
);

-- Create EPHONE table
CREATE TABLE EPHONE (
    EmployeeID INT,
    EPhone VARCHAR(15),
    PRIMARY KEY (EmployeeID, EPhone),
    FOREIGN KEY (EmployeeID) REFERENCES EMPLOYEE(EmployeeID)
);

-- Create PROMOTION table
CREATE TABLE PROMOTION (
    PromotionID INT PRIMARY KEY,
    Discount DECIMAL(5, 2),
    Name VARCHAR(255),
    Description VARCHAR(255),
    StartDay DATE,
    EndDay DATE
);

-- Create PRODUCT table
CREATE TABLE PRODUCT (
    ProductID INT PRIMARY KEY,
    Category VARCHAR(255),
    Description VARCHAR(255),
    PName VARCHAR(255),
    Price DECIMAL(10, 2),
    Weight DECIMAL(8, 2)
);

-- Create STORE table
CREATE TABLE STORE (
    StoreID INT PRIMARY KEY,
    Name VARCHAR(255),
    OpeningDate DATE,
    ContactInfo VARCHAR(255),
    Location VARCHAR(255)
);

-- Create STORE_MANAGER table
CREATE TABLE STORE_MANAGER (
    EmployeeID INT PRIMARY KEY,
    StoreID INT NOT NULL,
    FOREIGN KEY (StoreID) REFERENCES STORE(StoreID)
);

-- Create CASHIER table
CREATE TABLE CASHIER (
    EmployeeID INT PRIMARY KEY,
    Shift VARCHAR(255)
);

-- Create AT table
CREATE TABLE AT (
    ProductID INT,
    StoreID INT,
    NumberAtStore INT,
    PRIMARY KEY (ProductID, StoreID),
    FOREIGN KEY (ProductID) REFERENCES PRODUCT(ProductID),
    FOREIGN KEY (StoreID) REFERENCES STORE(StoreID)
);

-- Create INCLUDE table
CREATE TABLE INCLUDE (
    TransactionID INT,
    ProductID INT,
    NumberOfProductInBill INT,
    PRIMARY KEY (TransactionID, ProductID),
    FOREIGN KEY (TransactionID) REFERENCES BILL(TransactionID),
    FOREIGN KEY (ProductID) REFERENCES PRODUCT(ProductID)
);
