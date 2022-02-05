                                              # NEW CARS
                                                       #1.AUDI
def Audi_Q8():
    print(" ")
    a=open("new_audi_q8","r")
    print(a.read())
    a.close()
    print(" ")
    return
def Audi_Q3():
    print(" ")
    b = open("new_audi_q3", "r")
    print(b.read())
    b.close()
    print(" ")
    return
def Audi_A6():
    print(" ")
    c = open("new_audi_a6", "r")
    print(c.read())
    c.close()
    print(" ")
    return
                                                        #2.BMW
def BMW_X5():
    print(" ")
    d = open("new_bmw_x5", "r")
    print(d.read())
    d.close()
    print(" ")
    return
def BMW_X7():
    print(" ")
    e = open("new_bmw_x7", "r")
    print(e.read())
    e.close()
    print(" ")
    return
def BMW_Z4():
    print(" ")
    f = open("new_bmw_z4", "r")
    print(f.read())
    f.close()
    print(" ")
    return()
    # 3.VOLKSWAGEN
def VOLKSWAGEN_TIGUAN():                                  #3.VOLKSWAGEN
    print(" ")
    g = open("new_volks_tiguan", "r")
    print(g.read())
    g.close()
    print(" ")
    return()
def VOLKSWAGEN_POLO():
    print(" ")
    h = open("new_volks_polo", "r")
    print(h.read())
    h.close()
    print(" ")
    return()
def VOLKSWAGEN_GOLF():
    print(" ")
    i = open("new_volks_golf", "r")
    print(i.read())
    i.close()
    print(" ")
    return()
                                                             #4.MERCEDES
def MERCEDES_GLA():
    print(" ")
    j = open("new_mercedes_gla", "r")
    print(j.read())
    j.close()
    print(" ")
    return()
def MERCEDES_C_CLASS():
    print(" ")
    k = open("new_mercedes_c_class", "r")
    print(k.read())
    k.close()
    print(" ")
    return()
def MERCEDES_GLC():
    print(" ")
    l = open("new_mercedes_glc", "r")
    print(l.read())
    l.close()
    print(" ")
    return()
                                                           #5. TESLA
def TESLA_MODEL_3():
    print(" ")
    m = open("new_tesla_3", "r")
    print(m.read())
    m.close()
    print(" ")
    return()
def TESLA_MODEL_S():
    print(" ")
    n = open("new_tesla_s", "r")
    print(n.read())
    n.close()
    print(" ")
    return()
def TESLA_MODEL_Y():
    print(" ")
    o = open("new_tesla_y", "r")
    print(o.read())
    o.close()
    print(" ")
    return()
                                                     #code for used cars
def MERCEDES_E_CLASS_USED():                         #1.MERCERDES
    print(" ")
    p = open("used_mercedes_e", "r")
    print(p.read())
    p.close()
    print(" ")

    return()
def  MERCEDES_GL_CLASS_USED():
    print(" ")
    q = open("used_mercedes_e", "r")
    print(q.read())
    q.close()
    print(" ")
    return()
def MERCEDES_CLA_USED():
    print(" ")
    r = open("used_mercedes_e", "r")
    print(r.read())
    r.close()
    print(" ")
    return()
def VOLKSWAGEN_POLO_USED():                                  #2.VOLKSWAGEN
    print(" ")
    s = open("used_mercedes_e", "r")
    print(s.read())
    s.close()
    print(" ")
    return()
def  VOLKSWAGEN_PASSAT_USED():
    print(" ")
    t = open("used_mercedes_e", "r")
    print(t.read())
    t.close()
    print(" ")
    return()
def VOLKSWAGEN_VENTO_USED():
    print(" ")
    u = open("used_mercedes_e", "r")
    print(u.read())
    u.close()
    print(" ")
    return()
def BMW_520D_USED():                                        #3.BMW
    print(" ")
    u = open("used_mercedes_e", "r")
    print(u.read())
    u.close()
    print(" ")
    return()
def  BMW_730LD_USED():
    print(" ")
    u = open("used_mercedes_e", "r")
    print(u.read())
    u.close()
    print(" ")
    return()
def  AUDI_A4_USED():                                  #4.AUDI
    print(" ")
    u = open("used_mercedes_e", "r")
    print(u.read())
    u.close()
    print(" ")
    return()
def AUDI_A3_USED():
    print(" ")
    u = open("used_mercedes_e", "r")
    print(u.read())
    u.close()
    print(" ")
    return()
def FERRARI_USED():                                  #5.FERRARI
    print(" ")
    u = open("used_mercedes_e", "r")
    print(u.read())
    u.close()
    return()
option=0
while  option<4:

 def AutomobileDirectory():
    print("[1] NEW CARS")
    print("[2] USED CARS")
    print("[3] CAR SERVICE")
    print("[4] EXIT")
    print(" ")

 AutomobileDirectory()
 option = int(input("Please enter the option: "))

 if option == 1:
    # NEW CARS
    print(" ")
    print("CAR BRANDS")
    print("[1.1] AUDI")
    print("[1.2] BMW")
    print("[1.3] VOLKSWAGEN")
    print("[1.4] MERCEDES")
    print("[1.5] TESLA")
    print("[1.6] BACK")
    print(" ")

    option = float(input("Which Brand would you prefer: "))

    if option == 1.1:
        # AUDI
        print(" ")
        print("[1.11] AUDI Q8")
        print("[1.12] AUDI Q3")
        print("[1.13] AUDI A6")
        print("[1.14] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 1.11:
            # AUDI Q8
            Audi_Q8()


        elif option == 1.12:
            # AUDI Q3
            Audi_Q3()


        elif option == 1.13:
            # AUDI A6
            Audi_A6()

        elif option == 1.14:
            # BACK
            AutomobileDirectory()

        else:
            print(" ")
            print("invalid input")


    elif option == 1.2:
        # BMW
        print(" ")
        print("[1.21] BMW X5")
        print("[1.22] BMW X7")
        print("[1.23] BMW Z4 ROADSTER")
        print("[1.24] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 1.21:
           BMW_X5()               # BMW X5

        elif option == 1.22:
            BMW_X7()            # BMW X7

        elif option == 1.23:
           BMW_Z4()  # BMW Z4 ROADSTER


        elif option == 1.24:
            # BACK
            AutomobileDirectory()

        else:
            print(" ")
            print("invalid input")


    elif option == 1.3:
        # VOLKSWAGEN
        print(" ")
        print("[1.31] VOLKSWAGEN TIGUAN")
        print("[1.32] VOLKSWAGEN POLO")
        print("[1.33] VOLKSWAGEN GOLF")
        print("[1.34] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 1.31:
           VOLKSWAGEN_TIGUAN() # VOLKSWAGEN TIGUAN

        elif option == 1.32:
           VOLKSWAGEN_POLO()   # VOLKSWAGEN TIGUAN

        elif option == 1.33:

           VOLKSWAGEN_GOLF()   # VOLKSWAGEN GOLF


        elif option == 1.34:
            # BACK
            AutomobileDirectory()
        else:
            print(" ")
            print("Invalid Input")

    elif option == 1.4:
        # MERCEDES
        print(" ")
        print("[1.41] MERCEDES GLA")
        print("[1.42] MERCEDES C CLASS")
        print("[1.43] MERCEDES GLC")
        print("[1.44] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 1.41:
            # MERCEDES GLA
          MERCEDES_GLA()


        elif option == 1.42:
            # MERCEDES C CLASS
           MERCEDES_C_CLASS()


        elif option == 1.43:
            # MERCEDES GLC
          MERCEDES_GLC()


        elif option == 1.44:
            # BACK
            AutomobileDirectory()

        else:
            print(" ")
            print("Invalid Input")

    elif option == 1.5:
        # TESLA
        print(" ")
        print("[1.51] TESLA MODEL 3")
        print("[1.52] TESLA MODEL S")
        print("[1.53] TESLA MODEL Y")
        print("[1.54] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 1.51:
           TESLA_MODEL_3()   # TESLA MODEL 3

        elif option == 1.52:
           TESLA_MODEL_S()    # TESLA MODEL S


        elif option == 1.53:
           TESLA_MODEL_Y()    # TESLA MODEL Y


        elif option == 1.54:
            # BACK
            AutomobileDirectory()

        else:
            print(" ")
            print("Invalid Input")

    elif option == 1.6:
        AutomobileDirectory()

    else:
        print(" ")
        print("Invalid Input")


 elif option == 2:
    # OLD CARS
    print(" ")
    print("CAR BRANDS AVAILABLE")
    print("[2.1] MERCEDES")
    print("[2.2] VOLKSWAGEN")
    print("[2.3] BMW")
    print("[2.4] AUDI")
    print("[2.5] FERRARI")
    print("[2.6] BACK")
    print(" ")

    option = float(input("Which Brand would you prefer: "))

    if option == 2.1:
        # MERCEDES
        print(" ")
        print("[2.11] 2018 Mercedes-Benz E-Class Exclusive E 220d")
        print("[2.12] 2018 Mercedes-Benz GL-Class 220d 4MATIC Sport")
        print("[2.13] 2016 Mercedes-Benz CLA 200 CDI Sport")
        print("[2.14] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 2.11:
            # 2018 Mercedes-Benz E-Class Exclusive E 220d
            MERCEDES_E_CLASS_USED()

        elif option == 2.12:
            # 2018 Mercedes-Benz GL-Class 220d 4MATIC Sport
            MERCEDES_GL_CLASS_USED()

        elif option == 2.13:
            # 2016 Mercedes-Benz CLA 200 CDI Sport
            MERCEDES_CLA_USED()

        elif option == 2.14:
            # BACK
            AutomobileDirectory()

        else:
            print(" ")
            print("Invalid Input")

    if option == 2.2:
        # VOLKSWAGEN
        print(" ")
        print("[2.21] 2018 Volkswagen Polo 2015-2019 1.0 MPI Comfortline")
        print("[2.22] 2012 Volkswagen Passat Diesel Highline 2.0 TDI")
        print("[2.23] 2011 Volkswagen Vento Diesel Highline")
        print("[2.24] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 2.21:
            # 2018 Volkswagen Polo 2015-2019 1.0 MPI Comfortline
           VOLKSWAGEN_POLO_USED()

        elif option == 2.22:
            # 2012 Volkswagen Passat Diesel Highline 2.0 TDI
            VOLKSWAGEN_PASSAT_USED()

        elif option == 2.23:
            # 2011 Volkswagen Vento Diesel Highline
            VOLKSWAGEN_VENTO_USED()

        elif option == 2.24:
            # BACK
            AutomobileDirectory()

        else:
            print(" ")
            print("Invalid Input")


    elif option == 2.3:
        # BMW
        print(" ")
        print("[2.31] 2014 BMW 5 Series 520d Luxury Line")
        print("[2.32] 2018 BMW 7 Series 730Ld M Sport")
        print("[2.33] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 2.31:
            # 2014 BMW 5 Series 520d Luxury Line
            BMW_520D_USED()

        elif option == 2.32:
            # 2018 BMW 7 Series 730Ld M Sport
            BMW_730LD_USED()

        elif option == 2.33:
            # BACK
            AutomobileDirectory()

        else:
            print(" ")
            print("Invalid Input")

    elif option == 2.4:
        # AUDI
        print(" ")
        print("[2.41] 2012 Audi A4 2.0 TDI")
        print("[2.42] 2015 Audi A3 35 TDI Premium Plus")
        print("[2.43] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 2.41:
            # 2012 Audi A4 2.0 TDI
           AUDI_A4_USED()

        elif option == 2.42:
            # 2015 Audi A3 35 TDI Premium Plus
            AUDI_A3_USED()

        elif option == 2.43:
            # BACK
            AutomobileDirectory()

        else:
            print(" ")
            print("Invalid Input")

    elif option == 2.5:
        # FERRARI
        print(" ")
        print("[2.51] 2018 Ferrari GTC4Lusso T")
        print("[2.54] BACK")
        print(" ")

        option = float(input("Which Model would you prefer: "))

        if option == 2.51:
            # 2018 Ferrari GTC4Lusso T
            FERRARI_USED()
            print(" ")

        elif option == 2.54:
            # BACK
            AutomobileDirectory()

        else:
            print(" ")
            print("Invalid Input")

    elif option == 2.6:
        # BACK
        AutomobileDirectory()

    else:
        print(" ")
        print("Invalid Input")

 elif option == 3:
    # CAR SERVICE
    print(" ")
    print("[3.1] INTERM SERVICES")
    print("[3.2] FULL SERVICES")
    print("[3.3] MAJOR SERVICES")
    print("[3.4] BACK")
    print(" ")

    option = float(input("Select the above option to find brief information about service   : "))

    if option == 3.1:
        # INTERM SERVICE
        print(" ")
        sr = open("interm_service", "r")
        print(sr.read())
        sr.close()
        print(" ")

    elif option == 3.2:
        # FULL SERVICE
        print(" ")
        fl = open("full_service", "r")
        print(fl.read())
        fl.close()
        print(" ")

    elif option == 3.3:
        # MAJOR SERVICE
        print(" ")
        mj = open("major_service", "r")
        print(mj.read())
        mj.close()
        print(" ")

    elif option == 3.4:
        # BACK
        AutomobileDirectory()

    else:
        print(" ")
        print("Invalid Input")

else:
    # EXIT
    print("THANK YOU FOR VISITING")
    print("GOOD BYE")  # Automobile Directory


