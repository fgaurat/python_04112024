def main():
    a = 2
    b = 3
    c = a/b
    # r = f"a:{a}/b:{b}=c:{c:.2%}"
    r = f"{a=}/{b=}={c=:.2%}"
    print(r)

    v = "value"
    print(f"|{v:>10}|")
    print(f"|{v:<10}|")

    r = f"{a=}/{b=}={c=:>10.2%}"
    print(r)
    print(50*'-')
    a = 2
    b = 3
    c = a/b

    s = "{}/{} = {:.2%}".format(a, b, c)
    print(s)

    l = [1, 2, 3]
    # s = "{}, {}, {}".format(l[0],l[1],l[2])
    s = "{}, {}, {}".format(*l)
    print(s)
    s = "Bonjour {name} {first_name}".format(name="GAURAT", first_name="Fred")
    print(s)

    d = {
        "name": "GAURAT", 
        "first_name": "Fred"
    }
    s = "Bonjour {name} {first_name}".format(**d)
    print(s)


if __name__ == '__main__':
    main()
