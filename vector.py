#coding:utf-8
import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    #两个向量是否相等
    def __eq__(self, v):
        return self.coordinates == v.coordinates

    #向量相加
    def __add__(self,other):
        return Vector([x+y for x,y in zip(self.coordinates,other.coordinates)])
    
    #计算向量大小
    def calcMag(self):
        mag =  sum([x*x for x in self.coordinates])
     	return math.sqrt(mag)

    #计算方向向量
    def directVector(self):
        mag = self.calcMag()
        return Vector([x/mag for x in self.coordinates])

    #计算向量点积
    def calcPro(self,other):
        return self.calcMag()*other.calcMag()*self.calcCosAngle(other)
    #计算向量cos角度
    def calcCosAngle(self,other):
        return sum([x*y for x,y in zip(self.coordinates,other.coordinates)])/(self.calcMag()*other.calcMag())
    #计算向量角度
    def calcAngle(self,other):
        print self.calcCosAngle(other)
        return math.acos(self.calcCosAngle(other))

    #向量是否平行
    def clacVectorParalle(self,other):
        return abs(self.calcAngle(other))<1e-5
    #向量是否正交
    def clacVectorOrthogo(self,other):
        return abs(self.calcPro(other))<1e-5
    #计算普通数字乘以向量
    def __mul__(self,num):
        return Vector([round(x*num,3) for x in self.coordinates])

    def __sub__(self,other):
        return Vector([round(x-y,3) for x,y in zip(self.coordinates,other.coordinates)])
    #计算向量积
    def cross(self,other):
        x1,y1,z1 = self.coordinates
        x2,y2,z2 = other.coordinates
        return Vector([(y1*z2-y2*z1),-(x1*z2-x2*z1),(x1*y2-x2*y1)])

    #计算向量平行四边行面积
    def area(self,other):
        a = self.calcMag()
        b = other.calcMag () 
        return a*b*math.sin(self.calcAngle(other))




#-------------------b---向量加法--------------
print Vector([1,2,3])+Vector([1,2,3])
#----------------------向量大小--------------
vec1 = Vector([-0.221,7.437])
print  vec1.calcMag()

vec2 = Vector([-8.813,-1.331,-6.247])
print  vec2.calcMag()

#----------------------方向向量--------------
vec3 = Vector([5.581,-2.136])
print vec3.directVector();
vec4 = Vector([1.996,3.108,-4.554])
print vec4.directVector();
#----------------------向量积和角度计算--------------
vec5=  Vector([7.887,4.138])
vec6=  Vector([-8.802,6.776])
print vec5.calcPro(vec6);

vec7=  Vector([-5.955,-4.904,-1.874])
vec8=  Vector([-4.496,-8.755,7.103])
print vec7.calcPro(vec8);

vec9=  Vector([3.183,-7.627])
vec10=  Vector([-2.668,5.319])
print vec9.calcAngle(vec10);

vec11=  Vector([7.35,0.221,5.188])
vec12=  Vector([2.751,8.259,3.985])
print 180*vec11.calcAngle(vec12)/3.14159;

#----------------------计算向量是否平行或正交----------
vec13=  Vector([-7.579,-7.88])
vec14=  Vector([22.737,23.64])
print vec13.calcAngle(vec14);
print vec13.clacVectorOrthogo(vec14);

vec15=  Vector([-2.029,9.97,4.172])
vec16=  Vector([-9.231,-63639,-7.245])
print vec15.clacVectorParalle(vec16);
print vec15.clacVectorOrthogo(vec16);

vec17=  Vector([-2.328,-7.284,-1.214])
vec18=  Vector([-1.821,1.072,-2.94])
print vec17.clacVectorParalle(vec18);
print vec17.clacVectorOrthogo(vec18);


# vec13=  Vector([-7.579,-7.88])
# vec14=  Vector([22.737,23.64])
# print vec13.clacVectorParalle(vec14);
# print vec13.clacVectorOrthogo(vec14);

#计算vec15在vec16上的投影
#首先要找到vec16的方向向量
vec15 = Vector([3.039,1.879])
vec16 = Vector([0.825,2.036])
vecU16 = vec16.directVector()
#然后计算vec15和vecU16的点积
pro =  vec15.calcPro(vecU16)
#最后用点积乘方向向量就得出答案了
touyin15 = vecU16*pro
print touyin15


#计算两个向量的减法   a在b上投影+法向量=向量a   所以法向量 = a在b上投影 - 投影向量

vec17 = Vector([-9.88,-3.264,-8.159])
vec18 = Vector([-2.155,-9.353,-9.473])
vecU18 = vec18.directVector()
#然后计算vec15和vecU16的点积
pro =  vec17.calcPro(vecU18)
#最后用点积乘方向向量就得投影了
touyin17 = vecU18*pro
print vec17 - touyin17

#计算出投影和正交向量
vec19 = Vector([3.009,-6.172,3.692,-2.51])
vec20 = Vector([6.404,-9.144,2.759,8.718])
vecU20=vec20.directVector()
pro  =vec19.calcPro(vecU20)
touyin19 = vecU20*pro
print touyin19
print vec19-touyin19

#计算向量的积
vec21 = Vector([8.462,7.893,-8.187])
vec22 = Vector([6.984,-5.975,4.778])
resutlCross = vec21.cross(vec22)
print resutlCross

#计算向量围城的平行四边形的面积，或者用两个向量的积的大小也得得出
vec23 = Vector([-8.987,-9.838,5.031])
vec24 = Vector([-4.268,-1.861,-8.866])
print vec23.area(vec24)

#计算向量围城的三角形形的面积
vec25 = Vector([1.5,9.547,3.691])
vec26= Vector([-6.007,0.124,5.772])
print (vec25.area(vec26))/2

