def main():
    # Anton ki age ko directly 21 set kiya
    anton_age = 21

    # Beth ki age Anton se 6 saal zaida hai, thats why beth ki age main 6 add kiya
    beth_age = anton_age + 6

    # chen ki age beth say 20 saal zaida hai, thats why beth ki age main 20 add kiya
    chen_age = beth_age + 20

    # Drew ki age chaen ki age or anton ki age ka sum hai
    drew_age = chen_age + anton_age

    # ethen ki age chen ki age k equal hai , thats why ethen ki age chaen ki age k aqual set ki hai.
    ethan_age = chen_age

    # yahan sub ki age print ki gai hai.
    print(f"Anton is {anton_age}")
    print(f"Beth is {beth_age}")
    print(f"chen is {chen_age}")
    print(f"Drew is {drew_age}")
    print(f"Ethen is {ethan_age}")

# agar program ko directly run kiya ja raha ho to function execute ho
if __name__ == '__main__':
    main()