
create_address_table  = """
                    CREATE TABLE ADDRESS (
                        ID INT NOT NULL PRIMARY KEY,
                        country varchar(100),
                        city varchar(100),
                        street varchar(100),
                        postal varchar(100)
                        
                    )

"""

create_course_table = """
                    CREATE TABLE COURSE(
                        ID INT NOT NULL PRIMARY KEY,
                        code varchar(30),
                        maximum varchar(50)
                        minimum varchar(50)
                        
                    )

"""

create_employee_table = """
                    CREATE TABLE EMPLOYEE(
                        ID INT NOT NULL PRIMARY KEY,
                        firstName varchar(50),
                        lastName varchar(50),
                        phoneNumber varchar(30),
                        dateOfBirth varchar(20),
                        address varchar(50),
                        title varchar(50),
                        international int,
                        dateOfEmployment varchar(20)
                        
                    )
"""
create_enrollment_table = """
                    CREATE TABLE ENROLLMENT(
                        course varchar(50),
                        employee varchar(50)
                    )

"""
create_trainer_table = """
                   CREATE TABLE TRAINER(
                       ID INT NOT NULL PRIMARY KEY,
                       firstName varchar(50),
                       lastName varchar(50),
                       phoneNumber varchar(30),
                       address varchar(50),
                       domain varchar(50),
                       salary int,
                       courses varchar(100),
                       got_raise varchar(20)
                   )

"""
