from Trainer import Trainer
from Enrollment import Enrollment
from Employee import Employee
from Course import Course
from Address import Address
from mysql.connector import connect, Error,connection
from datetime import datetime
from DB_queries import create_address_table,create_course_table,create_employee_table,create_enrollment_table,create_trainer_table
from getpass import getpass

dict_address = {
    'addresses': {
                    'adr1': ['Poland', 'Krosno', 'Pilsudskiego 3', '20-132'],
                    'adr2': ['Germany', 'Berlin', 'Adolfa 3', '12-677'],
                    'adr3': ['Poland', 'Krakow', 'Krakowska 3', '11-112'],
                    'adr4': ['Poland', 'Krakow', 'Ruczaj 3', '22-362'],
                    'adr5': ['Poland', 'Tarnow', 'Tarnowska 13', '32-322'],
                    'adr6': ['Poland','Krakow','Pradnik 13', '11-111'],
                    'adr7': ['France','Paris','Saint Street 1', '55-213']
        }
}

dict_person = {
    'persons': {
                    'emp1': ['Artur', 'Skrzeta', '+48 727 929 994', datetime(1993,4,20)],
                    'emp2': ['Zbyszek', 'Kowal', '+48 333 929 111', datetime(1990,2,21)],
                    'emp3': ['Maria', 'Nowak', '+48 123 555 678', datetime(1996,11,1)],
                    'emp4': ['Karol', 'Zych', '+48 455 155 998', datetime(1991,3,11)],
                    'tra1': ['John', 'Smith', '+48 566 532 123', datetime(1987,12,24)],
                    'tra2': ['Mike', 'Thomson', '+48 987 924 001', datetime(1985,9,8)]
        }
}

dict_employee = {
    'employees' : {
                    'emp1': ['Data Analyst', False, datetime(2019,1,20)],
                    'emp2': ['Software Enginner', True, datetime(2018,1,1)],
                    'emp3': ['Strategic Buyer', False, datetime(2014,7,22)],
                    'emp4': ['Operational Buyer', False, datetime(2015,11,1)]
        }
}

dict_trainer = {
    'trainers': {
                    'tra1': ['Data Analysis with Python', 10000.00],
                    'tra2': ['RPA Specialization', 8000.00]
        }
}

dict_course = {
    'courses' : {
                    'cou1': ['Basic Python','BPY001', 3, 2],
                    'cou2': ['Intermediate Python','IPY001', 3, 2],
                    'cou3': ['Advanded Python','APY001', 3, 2],
                    'cou4': ['RPA introduction','RPAI001', 3, 2],
                    'cou5': ['RPA for SAP automation','RPAS001', 3, 2]
        }
}

def data_objects(dict_data) :
    objects_list = []
    main_key = list(dict_data.keys())
    
    if main_key[0] == 'addresses' :
        for inner_key in dict_data[main_key[0]] :
               a = Address(inner_key,
                            dict_data[main_key[0]][inner_key][0],
                            dict_data[main_key[0]][inner_key][1],
                            dict_data[main_key[0]][inner_key][2],
                            dict_data[main_key[0]][inner_key][3])
               objects_list.append(a)
             
        
    if main_key[0] == 'employees' :
        for inner_key in dict_data[main_key[0]] :
            e = Employee(inner_key,
                         dict_person['persons'][inner_key][0],
                            dict_person['persons'][inner_key][1],
                            dict_person['persons'][inner_key][2],
                            dict_person['persons'][inner_key][3],
                            dict_data[main_key[0]][inner_key][0],
                            dict_data[main_key[0]][inner_key][1],
                            dict_data[main_key[0]][inner_key][2])
            objects_list.append(e)
            
    if main_key[0] == 'trainers' :
        for inner_key in dict_data[main_key[0]] :
            t = Trainer(inner_key,
                            dict_person['persons'][inner_key][0],
                            dict_person['persons'][inner_key][1],
                            dict_person['persons'][inner_key][2],
                            dict_person['persons'][inner_key][3],
                            dict_data[main_key[0]][inner_key][0],
                            dict_data[main_key[0]][inner_key][1])
            objects_list.append(t)
            
    if main_key[0] == 'courses' :
        for inner_key in dict_data[main_key[0]] :
             c = Course(inner_key,
                            dict_data[main_key[0]][inner_key][0],
                            dict_data[main_key[0]][inner_key][1],
                            dict_data[main_key[0]][inner_key][2],
                            dict_data[main_key[0]][inner_key][3])
             objects_list.append(c)
    
    return objects_list

def associate_address_to_person(persons,addresses) :
    for p in persons:
        if p.id == 'emp1': p.add_address([addresses[0], addresses[2]])
        if p.id == 'emp2': p.add_address(addresses[3])
        if p.id == 'emp3': p.add_address(addresses[1])
        if p.id == 'emp4': p.add_address(addresses[4])
        if p.id == 'tra1': p.add_address(addresses[6])
        if p.id == 'tra2': p.add_address(addresses[5])
    
def associate_trainer_to_course(courses, trainers):
    for c in courses:
        if c.id == 'cou1':
            c.add_trainer(trainers[0])
            trainers[0].add_course(c)
        if c.id == 'cou2':
            c.add_trainer(trainers[0])
            trainers[0].add_course(c)
        if c.id == 'cou3':
            c.add_trainer(trainers[0])
            trainers[0].add_course(c)
        if c.id == 'cou4':
            c.add_trainer(trainers[1])
            trainers[1].add_course(c)
        if c.id == 'cou5':
            c.add_trainer(trainers[1])
            trainers[1].add_course(c)
            
def make_enrollment(employee, course):
    en = Enrollment(employee, course)
    employee.add_enrollment(en)
    course.add_enrollment(en)
    return en

def print_objects(list):
    for item in list:
        print(item)

    

def connect_db_and_create_tables():
    queries = [
        create_address_table,
        create_course_table,
        create_employee_table,
        create_enrollment_table,
        create_trainer_table
    ]
    
    try :
        with connect(
            host = 'localhost',
            user = input('Enter Username : '),
            password = getpass('Enter Password : '),
            
        ) as connection :
            create_db_query = "CREATE DATABASE SCHOOL_SYSTEM"
            with connection.cursor() as cursor :
                cursor.execute(create_db_query)
    except Error as e :
        print(e)
    
          
    for query in queries :
        cursor.execute(query)
        connection.commit()
   
 
        
def insert_values_into_Address_table(addresses) :
         for address in addresses:
             with connection.cursor() as cursor :
                cursor.execute("INSERT INTO tblAddress VALUES ('" + address.id +
                                                "','" + address.country +
                                                "','" + address.city +
                                                "','" + address.street +
                                                "','" + address.postal + "')")
       
                connection.commit()
         
def insert_values_into_Trainers_table(trainers) :
    for trainer in trainers :
        with connection.cursor() as cursor :
            
            cursor.execute("INSERT INTO tblTrainer VALUES ('" + trainer.id +
                                                "','" + trainer.firstName +
                                                "','" + trainer.lastName +
                                                "','" + trainer.phoneNumber +
                                                "','" + str(trainer.dateOfBirth) +
                                                "','" + trainer.convert_addresses_into_string() +
                                                "','" + trainer.domain +
                                                "','" + str(trainer.salary) +
                                                "','" + trainer.convert_courses_into_string() +
                                                "','" + str(trainer.got_raise) +
                                                "')")
            connection.commit()
            
def insert_values_into_emplyees_table(employee) :
    for emp in employee :
        with connection.cursor() as cursor :
            cursor.execute("INSERT INTO tblEmployee VALUES ('" + emp.id +
                                                "','" + emp.firstName +
                                                "','" + emp.lastName +
                                                "','" + emp.phoneNumber +
                                                "','" + str(emp.dateOfBirth) +
                                                "','" + emp.convert_addresses_into_string() +
                                                "','" + emp.title +
                                                "','" + str(emp.international) +
                                                "','" + str(emp.dateOfEmployment) +
                                                "')")
            connection.commit()

def insert_values_into_course_table(courses) :
    for cos in courses :
        with connection.cursor() as cursor :
            
            cursor.execute("INSERT INTO tblCourse VALUES ('" + cos.id +
                                                "','" + cos.code +
                                                "','" + str(cos.minimum) +
                                                "','" + str(cos.maximum) +
                                                "')")
            connection.commit()

def insert_values_into_enrollment_table(enrollments) :
    for enroll in enrollments :
        with connection.cursor() as cursor :
            
            cursor.execute("INSERT INTO tblEnrollment VALUES ('" + enroll.employee.id +
                                                "','" + enroll.course.code +
                                                "')")
            connection.commit()

def select_data_from_database(tableName) :
    with connection.cursor() as cursor :
        cursor.execute("SELECT * FROM " + tableName)
        myData = cursor.fetchall()
        for data in myData :
            print(data)

def main() :
    
    # create the objects
    addresses = data_objects(dict_address)
    trainers = data_objects(dict_trainer)
    courses = data_objects(dict_course)
    employees = data_objects(dict_employee)
    
    
    # Make the associations
    associate_address_to_person(employees,addresses)
    associate_trainer_to_course(courses,trainers)
    associate_address_to_person(trainers,addresses)
    
    global enrollments
    enrollments = []
    enrollments.append(make_enrollment(employees[0], courses[0]))
    enrollments.append(make_enrollment(employees[1],courses[3]))
    
    #cobjects db
    connect_db_and_create_tables()
    insert_values_into_Address_table(addresses)
    insert_values_into_emplyees_table(employees)
    insert_values_into_Trainers_table(trainers)
    insert_values_into_course_table(courses)
    insert_values_into_enrollment_table(enrollments)
    
    
    
    connection.close()

if __name__ == "__main__" :
    main()
    
    