

def getBondPrice_Z(face, couponRate, times, yc):
 pvcfsum =0
 cf = couponRate*face
 for y,t in zip(yc,times):
   pv =(1+y)**(-t)
   pvcf = pv*cf
   pvcfsum += pvcf

 bondprice = pvcfsum + pv*face
 return(bondprice) 

