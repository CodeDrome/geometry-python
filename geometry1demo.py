import geometry1 as g1


def main():
    
    print("-----------------")
    print("| codedrome.com |")
    print("| Geometry 1    |")
    print("-----------------\n")

    g1.line((1,5), (9,9))

    g1.triangle((1,1), (7,1), (1,4))

    g1.arc((1,1), 0.5, 0.0, 90.0)
    g1.arc((1,4), 0.5, 270.0, 63.0)
    g1.arc((7,1), 0.5, 153.0, 26.0)

    g1.circle((7.0,5.0), 2.0)

    g1.draw((0.0, 10.0), (0.0, 10.0), (0,11), (0,11), "Geometry 1")


if __name__ == "__main__":

    main()

