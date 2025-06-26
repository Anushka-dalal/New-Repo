def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("*********************************************")
            result = func(*args, **kwargs)
            result += 10
            print("After modifying function = ",result)
            print("*********************************************")
            return result
        return wrapper

 


