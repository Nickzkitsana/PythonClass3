import math as m

def pracSlide55():
    print('Senior : 65 up\nAdult : 18-64\nJunior: 4-17\nChild : 0-3')
    senior , adult , junior , child = input('Enter number of Senior,Adult,Junior,Child : ').split(',')
    total = (float(senior)*19.95)+(float(adult)*22.95)+(float(junior)*14.95)+(float(child)*0)
    print('Total of Ticket : ${0:,.2f}'.format(total))


def pracSlide57():
    Fname , Lname = input('Please Enter your full name : ').split()
    print('Your Thai-Nichi student E-mail is "{0}.{1}_st@tni.ac.th"'
          .format(Lname[:2].lower(),Fname.lower()))

def pracSlide146():
    point1 = 5,5
    point2 = (2,1)
    distance = m.sqrt(m.pow((float(point2[0]-float(point1[0]))),2) + m.pow((float(point2[1]-float(point1[1]))),2))
    print('Point1 = {0}'.format(point1))
    print('Point2 = {0}'.format(point2))
    print('Distance between two points = {0:.2f}'.format(distance))


def pracSlide148():
    weight = (62.5,78,50,42,84,65.5,48,53.5,43)
    avg = sum(weight) / len(weight)
    print('Weight : {0}\n'.format(weight))
    line()
    print('Maximum weight of {0} persons = {1}'.format(len(weight),max(weight)))
    print('Minimum weight of {0} persons = {1}'.format(len(weight),min(weight)))
    print('Average weight of {0} persons = {1:.2f}'.format(len(weight),avg))
    line()
    print('No. of weight above average = {0}'.format(aboveavg(weight)))
    print('No. of weight below average = {0}'.format(belowavg(weight)))
    print('No. of weight equal average = {0}'.format(equalavg(weight)))
    line()

def aboveavg(v):
    count=0
    for i in v:
        if i > sum(v)/len(v):
            count+=1
    return count

def belowavg(v):
    count=0
    for i in v:
        if i < sum(v)/len(v):
            count+=1
    return count

def equalavg(v):
    count=0
    for i in v:
        if i == sum(v)/len(v):
            count+=1
    return count

def line():
    print('*'*50)

def checkNumber(*num,see):
    if(see.lower() == 'max-min'):
        return max(num) , min(num)
    elif(see.lower() == 'ab-bl-av'):
        return aboveavg(num),belowavg(num)


