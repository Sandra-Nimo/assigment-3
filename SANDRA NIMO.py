#NAME:         BOAMAH NIMO SANDRA
#INDEX NUMBER: 6932721
#GITHUB 



                  #COMPUTER PROGRAMMING ASSIGNMENT
import numpy as np
import math as mth
w=10    #INTENSITY OF LOAD(kM/m)
l=12    #LENGHT OF BEAM(m)
 

          #QUESTION A
x1=0        
M1= (w*(-6*x1**2+6*l* x1 - l ** 2 )) / 12    #M1=bending moment of beam when x=0
V1 =w*((l/2)-x1)                             #V1=shear force of the beam when x=0


x2=l
M2=(w*(-6*x2**2+6*l*x2-l**2))/12            #M2=bending moment of beam when x=l
v2=w*((l/2)-x2)                             #V2=shear force on the beam when x=l

                     #QUESTION B
#when bending moment =0, using the almighty formula to find the points at which they occur 
a=-6
b=6*l
c=-l**2-(12/w)

root1=(-b+mth.sqrt(b**2-4*a*c))/(2*a)      #root1=the first point at which M=o    
root2=(-b-mth.sqrt(b**2-4*a*c))/(2*a)      #root2=the second point at which M=0


                 #QUESTION C
#when shear force =0,
x3=l/2                          #x3 is the point where shear force is zero
 

               #QUESTION D

x4=np.arange(0,12.01,0.01)              #x4 shows the range of values of lenght on the beam at interval 0.01mm
M3=(w*(-6*x4**2+6*l*x4-l**2))/12        #M3=thebending moment at the various intervals of lenght

                #QUESTION E    
V3=w*((l/2)-x4)                       #V3=shear force at each step

                #QUESTION F
AM=np.abs(M3)                        #AM=absolute bending moment  
T=min(AM)  #let T be the minimum absolute bending moment from question D              
                #using the almighty formula to find the pont at which the absolute values occur
k=-6
p=6*l                
q=-l**2-12*T/w                

root3=(-p**2+mth.sqrt(p**2-4*k*q))/(2*k)   #root3=the point at which the absolute minimum bending moment occurs
root4=(-p**2-mth.sqrt(p**2-4*k*q))/(2*k)   #root4=the point at which the absolute minimum bending moment occurs

                #QUESTION G
E1=((root1-root3)/root1*100)           #E1= 1st relative error between the estimated point
E2=((root4-root2)/root4*100)           #E2=2nd relative error between the estimated point

                #QUESTION H
R=max(M3)            #R is the maximum bending momebt on the beam
                #using the almighty formula;
s=-6
u=6*l
f=-(l**2-(12*R/w))

point1=(-u**2+mth.sqrt(u**2-4*s*f))/2*s    #point1=point at which the maximum bending moment occurs
point2=(-u**2-mth.sqrt(u**2-4*s*f))/2*s    #point2=point at which the maximum bending moment occurs

j=min(M3)                                #j=value of the mimimun bending moment
                  #using the almighty formula to find the points at which j occurs,
point3=(-u**2+mth.sqrt(u**2-4*s*j))/2*s   #point3= point at which minimum bending moment occurs
point4=(-u**2-mth.sqrt(u**2-4*s*j))/2*s   #point4=point at which minimuum bending moment occurs