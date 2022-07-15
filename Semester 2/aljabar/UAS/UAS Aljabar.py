# Python versi 3.9
#nama anggota kelompok
# 1. Edo Kurniawan              (211240001183)
# 2. Muhammad Arif Hidayanto    (211240001205)
# 3. Bintang Radya D.I.         (211240001142)
# 4. Dhintya Aprilia Setyani    (211240001194)
# 5. Fitri Desita Sari          (211240001103)
# 6. Muhammad Veriel Surya      (211240001171)

print ("""
---------------------------------------------------------------------
\t\t\t UAS Aljabar Linier \t\t\t
---------------------------------------------------------------------""")
print ()

def menu():
    print ('\t\t\t\t Menu  \t\t')
    print ('\t\t\t    |------------|\t')
    print ()
    print ()
    print ('''\t    1. Penyelesaian matriks menggunakan metode cramer
            2. invers matriks ordo 2x2
            3. transpose matriks ordo m x n
            4. keluar''')
    print()
    print()

    while True:
        pilih = input ('\t\tMasukkan pilihan : ')
        if pilih == '1':
            print()
            print ("""
  ====================================================================
                Penyelesaian matriks menggunakan metode cramer
  ====================================================================""")
            print()
            print()
            cramer()
            break
        elif pilih == '2':
            print()
            
            print ("""====================================================================
                Anda memilih Invers matriks 2x2
====================================================================""")
            print()
            print()
            invers()
            break
        elif pilih == '3':
            print ("""====================================================================
                  transpose matriks ordo m x n
====================================================================""")
            print()
            transpose()
            break
        elif pilih == '4':
            print ()
            print ("**************************** Terima Kasih ***************************")
            break
            exit()
        elif not pilih :
                print ('\t\tMaaf anda harus memasukkan pilihan.')
        else :
                print ('\t\tMaaf anda harus memasukkan pilihan.')
def cramer():
    print()
    print ("""\tDengan format :
    
        [ a11 a12 | b1]
        [ a21 a22 | b2]""")
    print()
    print()
    a11 =input('\tmasukkan nilai a11 : ')
    a12 =input('\tmasukkan nilai a12 : ')
    a21 =input('\tmasukkan nilai a21 : ')
    a22 =input('\tmasukkan nilai a22 : ')
    b1  =input('\tmasukkan nilai b1  : ')
    b2  =input('\tmasukkan nilai b2  : ')
    print()
    print()
    print("\t[",a11,a12,"|",b1,"]")
    print("\t[",a21,a22,"|",b2,"]")
    print()
    
    print("\tmetode det.ekspansi Kofaktor:")
    print()
    print("\tMatriks (A) = ")
    print("\t[",a11,a12,"]")
    print("\t[",a21,a22,"]")
    print()

    print("\tMatriks (A1) = ")
    print("\t[",b1,a12,"]")
    print("\t[",b2,a22,"]")
    print()

    print("\tMatriks (A2) = ")
    print("\t[",a11,b1,"]")
    print("\t[",a21,b2,"]")
    print()

    print("\tMenghitung Determinan Matrix A,A1,A2 : ")
    print()
    print("\tDeterminan A : ")
    A = (int(a11)*int(a22)- int(a12)* int(a21))
    print("\tDet A = ",A)
    print()

    print("\tDeterminan A1 : ")
    print()
    A1 = (int(b1)*int(a22)- int(a12)* int(b2))
    print("\tDet A1 = ",A1)
    print()

    print("\tDeterminan A2 : ")
    print()
    A2 = (int(a11)*int(b2)- int(b1)* int(a21))
    print("\tDet A2 = ",A2)
    print()

    X = int(A1)/int(A)
    print("\tNilai X : ",X)
    Y = int(A2)/int(A)
    print("\tNilai Y : ",Y)

    print ()
    print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
    tanya = input ('                   coba lagi?(y/t) : ')
    if tanya == 'y':
      print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
      cramer()
    else :
      print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
      menu()
def invers():
    print("""
    A = [  a  b  ]
        [  c  d  ]
        
    Rumus :
    
    A^-1 = [   d  -b  ] * 1/(a*d - b*c)
           [  -c   a  ]
    """)
    a = input("\tMasukkan a = ")
    b = input("\tMasukkan b = ")
    c = input("\tMasukkan c = ")
    d = input("\tMasukkan d = ")
    
    print ("""
    A = [ """,a,"""  """,b,""" ]
        [ """,c,"""  """,d,""" ]
    """)
    
    hasil = int (int(a)*int(d) - int(b)*int(c))
    print ("\tdet A : ",hasil)
    
    if hasil == 0:
        print ("matriks ini tidak memiliki invers atau disebut matriks singular")
        print()
        print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
    else:
      a1 = float (int(a)*(1/hasil))
      b1 = float (int(b)* (-1)*(1/hasil))
      c1 = float (int(c)* (-1) *(1/hasil))
      d1 = float (int(d)*(1/hasil))
      print ("""
      A^-1 = [ """,d1,"""  """,b1,""" ]
             [ """,c1,"""  """,a1,""" ]
       """)
      print()
      print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
    tanya = input ('                      coba lagi?(y/t) : ')
    if tanya == 'y':
      print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
      invers()
    else :
      print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
      menu()
      
def transpose():
    print()
    p = int (input("masukkan jumlah baris : "))
    q = int (input("masukkan jumlah kolom : "))
    print()
    print ("matriks1:")
    print()
    matriks1 = [[int(input("  ")) for i in range (q)] for j in range (p)]
    print()
    print ("matriks1 : ")
    print()
    for i in range (p):
      for j in range (q):
        print (format(matriks1[i][j],"<4"),end="")
      print()
    hasil = [[0 for i in range (p) ] for j in range (q)]
    for i in range (q):
      for j in range (p):
        hasil[i][j] = matriks1[j][i]
    print()
    print ("hasil transpose: ")
    print()
    for i in range (q):
      for j in range (p):
        print (format(hasil[i][j],"<4"),end="")
      print()
    print()
    print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
  
    tanya = input ('                      coba lagi?(y/t) : ')
  
    if tanya == 'y':
       print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
       transpose()
    else :
       print ('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')
       menu()
menu()


