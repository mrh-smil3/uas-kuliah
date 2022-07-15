# Pyhton 2.7
# TUGAS UAS Kalkulus II
# 1. Edo Kurniawan              (211240001183)
# 2. Muhammad Arif Hidayanto    (211240001205)
# 3. Bintang Radya D.I.         (211240001142)
# 4. Dhintya Aprilia Setyani    (211240001194)
# 5. Fitri Desita Sari          (211240001103)
# 6. Muhammad Veriel Surya      (211240001171)

import math

print """
*********************************************************************
                            UAS Kalkulus II
*********************************************************************
"""
def menu():
    print '''
                         **********************
                         *       Pilihan     *
                         **********************
                         1. Panjang kurva
                         2. Luas daerah yang diarsir
                         3. volume benda putar ke sumbu y
                         4. keluar'''
    print ""
    print ""
    
    while True:
        pilih = raw_input ('                Masukkan pilihan : ')
        if pilih == '1':
            print ""
            print """

********************************************************************
  *                     menghitung panjang kurva                 *
********************************************************************"""
            print""
            print""
            pjkurva()
            break
        elif pilih == '2':
            print""
            
            print """

********************************************************************
 *               menghitung luas daerah yang diarsir              *
********************************************************************"""
            print""
            print""
            luas()
            break
        elif pilih == '3':
            print """

********************************************************************
    *            menghitung volume benda putar ke sumbu y        *
********************************************************************"""
            print""
            volume()
            break
        elif pilih == '4':
            print ""
            print "----------------------------     DONE     --------------------------"
            break
            exit()
        elif not pilih :
                print 'Maaf anda harus memasukkan pilihan.'
        else :
                print 'tMaaf anda harus memasukkan pilihan.'

def pjkurva():
  a = raw_input("masukkan nilai a = ")
  b = raw_input("masukkan nilai b = ")
  x1= raw_input("masukkan nilai m(x1) = ")
  x2= raw_input("masukkan nilai k(x2) = ")
  print""
  a1=int(a)
  b1=int(b)
  m = int(x1)
  k = int(x2)
  
  t= 2*a1
  kuad = t**2
  rumx1 = (1+ kuad * m**2)**3
  rum2x1 = math.sqrt(rumx1)
  rum3x1 = rum2x1/(3*kuad)
  
  rumx2 = (1+ kuad * k**2)**3
  rum2x2 = math.sqrt(rumx2)
  rum3x2 = rum2x2/(3*kuad)
  
  pj = rum3x1 - rum3x2
  print "panjang kurva  = ",pj
  print ''
  print '********************************************************************'

  tanya = raw_input ('                   coba lagi?(y/t) : ')
  print''

  if tanya == 'y':
     print '********************************************************************'
     pjkurva()
  else :
      print '********************************************************************'
      menu()


def luas():
    a = raw_input("masukkan nilai a = ")
    b = raw_input("masukkan nilai b = ")
    x1= raw_input("masukkan nilai m(x1) = ")
    x2= raw_input("masukkan nilai k(x2) = ")
    print""
    a1=int(a)
    b1=int(b)
    m = int(x1)
    k = int(x2)
    r1 = a1/3
    print "= %sx^3 + %sx](%s, %s)"%(r1,b,m,k)
    nilai1 = r1 * m**3 + b1 * m
    nilai2 = r1 * k**3 + b1 * k
    print "(x=m=%s) = %s(%s)^3 + %s x (%s)"%(m,r1,m,b1,m)
    print "(x=k=%s) = %s(%s)^3 + %s x (%s)"%(k,r1,k,b1,k)
    hasil = nilai1 - nilai2
    print """luas    = (x=%s) - (x=%s)
            = %s - %s
            = %s"""%(m,k,nilai1,nilai2,hasil)
    print '********************************************************************'

    tanya = raw_input ('                   coba lagi?(y/t) : ')

    if tanya == 'y':
      print '********************************************************************'
      luas()
    else :
      print '********************************************************************'
      menu()


def volume():
    pi = 3.14
    print""
    print "metode kulit tabung"
    print""
    a = raw_input("masukkan nilai a = ")
    b = raw_input("masukkan nilai b = ")
    x1= raw_input("masukkan nilai m(x1) = ")
    x2= raw_input("masukkan nilai k(x2) = ")
    print""
    a1=int(a)
    b1=int(b)
    m = int(x1)
    k = int(x2)
    
    n1 = a1/4 * m**4 + b1/2 * m**2
    n2 = a1/4 * k**4 + b1/2 * k**2
    print "= %s/4 x^4 + %s/4 x^2 ](%s,%s)"%(a,b,m,k)
    print "(x=m=%s) = %s/4 (%s)^4 + %s/4 (%s)^2]"%(m,a,m,b,m)
    print "(x=k=%s) = %s/4 (%s)^4 + %s/4 (%s)^2]"%(k,a,k,b,k)
    print ""
    print "= 2 x pi x ((n=m)-(n=k))"
    print "= 2 x 3.14 x (%s - %s)"%(n1,n2)
    ha = 2*pi*(n1-n2)
    print "volume = ",ha
    print '********************************************************************'

    tanya = raw_input ('                   coba lagi?(y/t) : ')

    if tanya == 'y':
      print '********************************************************************'
      volume()
    else :
      print '********************************************************************'
      menu()
menu()



         
