def main():
    
    print("calculate the number of seconds in a year")
    one_year_days = 365       
    one_day_hour = 24
    one_hour_min =  60
    one_min_sec =  60

    # Total sec in a year calculate karna
    total_second = one_year_days * one_day_hour * one_hour_min * one_min_sec

    # result print karna
    print(f"There are {total_second} second in a year !")

if __name__ == '__main__':
    main()