
def getBondPrice_E(face, couponRate, m, yc):
 pvcfsum =0
 cf = couponRate*face
 for i,y in enumerate(yc):
    pv =(1+y)**(-(i+1))
    pvcf = pv*cf
    pvcfsum += pvcf
    
 bondprice = pvcfsum + pv*face
 return(bondprice)   


