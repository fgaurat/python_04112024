from CustomerDAO import CustomerDAO


def filter_male(stream):
    for data in stream:
        if data.gender == "Male":
            yield data
    
    
def main():
    dao = CustomerDAO('customers_db.db')
    
    customers = dao.find_all()
    male_customers = filter_male(customers)
    
    # print(len(customers))    
    for customer in male_customers:
        print(customer)

if __name__=='__main__':
    main()
