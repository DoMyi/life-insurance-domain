import datetime as dt
import random as r
import sys

class Customer:
    
    def __init__(self, idnum, name, gender, dob, addressObj = None, contactObj = None):
        self.__id = idnum
        self.__name = name
        self.__gender = gender
        self.__dob = dob
        self.__address = addressObj
        self.__contact = contactObj
        self.__policies = dict()


    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getDOB(self):
        return self.__dob
    def getAddress(self):
        return self.__address
    def getContact(self):
        return self.__contact
    def getGender(self):
        return self.__gender
    def getPolicies(self):
        return self.__policies.values()
    def getPolicy(self, pid):
        return self.__policies[pid]

    def setId(self,idnum):
        self.__id = idnum
    def setName(self, name):
        self.__name = name
    def setDOB(self, dob):
        self.__dob = dob
    def setAddress(self, addressObj):
        self.__address = addressObj
    def setContact(self, contactObj):
        self.__contact = contactObj
    def setGender(self, gender):
        self.__gender = gender

    def addPolicy(self, policy):
        self.__policies[policy.getId()] = policy 


class Address:
    
    def __init__(self, hno, city, street, pincode, landmark = None):
        self.hno = hno
        self.city = street
        self.pincode = pincode
        self.landmark = landmark

class Contact:

    def __init__(self, primemail, phno, secemail = None, landline = None):
        self.primemail = primemail
        self.secemail = secemail
        self.phno = phno
        self. landline = landline

class Policy:

    def __init__(self, pid, startdate, matdate, riskdate, term, payfreq):
        self.__id = pid
        self.__startdate = startdate
        self.__matdate = matdate
        self.__riskdate = riskdate
        self.__term = term
        self.__payfreq = payfreq
        self.__nominees = dict()
        self.__benefits = set()

    def getId(self):
        return self.__id
    def getStartDate(self):
        return self.__startdate
    def getMaturityDate(self):
        return self.__matdate
    def getRiskDate(self):
        return self.__riskdate
    def getTerm(self):
        return self.__term
    def getPaymentFrequency(self):
        return self.__payfreq
    def getNominee(self, nid):
        return self.__nominees[nid]
    def getNominees(self):
        return self.__nominees.values()
    def getBenefits(self):
        return list(self.__benefits)
    

    def setId(self, pid):
        self.__id = pid
    def setStartDate(self, startdate):
        self.__startdate = startdate
    def setMaturityDate(self, matdate):
        self.__matdate = matdate
    def setRiskDate(self, riskdate):
        self.__riskdate = riskdate
    def setTerm(self, term):
        self.__term = term
    def setPaymentFrequency(self, payfreq):
        self.__payfreq = payfreq

    def addNominee(self, nominee):
        self.__nominees[nominee.getId()] = nominee
    def addBenefit(self, benefit):
        self.__benefits.add(benefit)

class Nominee:
    
    def __init__(self, nid, name, rel, share):
        self.__id = nid
        self.__name = name
        self.__rel = rel
        self.__share = share

    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getRelationship(self):
        return self.__rel
    def getShare(self):
        return self.__share

    def setId(self, nid):
        self.__id = nid
    def setName(self, name):
        self.__name = name
    def setRelationship(self, rel):
        self.__rel = rel
    def setShare(self, share):
        self.__share = share


class Benefit:

    def __init__(self, name, bcode, sassured, premium, bgroup = None):
        self.__bcode = bcode
        self.__bgroup = bgroup
        self.__sassured = sassured
        self.__name = name
        self.__premium = premium
    def getBenefitName(self):
        return self.__name
    def getBenefitCode(self):
        return self.__bcode
    def getBenefitGroup(self):
        return self.__bgroup
    def getSumAssured(self):
        return self.__sassured
    def getPremium(self):
        return self.__premium

    def setBenefitCode(self, bcode):
        self.__bcode = bcode
    def setBenefitGroup(self, bgroup):
        self.__bgroup = bgroup
    def setSumAssured(self, sassured):
        self.__sassured = sassured
    def setBenefitName(self, name):
        self.__name = name
    def setPremium(self, premium):
        self.__premium = premium

class Master:

    def __init__(self):
        self.__customers = dict()
        self.__plans = ["Smart Life","Life Protect","Nirvana"]

    def getCustomer(self, idnum):
        return self.__customers[idnum]
    def getAllCustomers(self):
        return self.__customers.values()

    def addCustomer(self, customerObj):
        self.__customers[(customerObj.getId())] = customerObj
    def getAllPlans(self):
        return self.__plans

##################################################### ~Driver Program~ ###############################################################

print("~"*30 + "Life Insurance Domain" + "~"*30)
admin = Master()
plans = {"smart life":["Death Benefit", "Accidental", "Critical Illness" , "Permanent Disability"], "life security": ["Death Benefit", "Accidental", "Critical Illness" , "Permanent Disability"], "nirvana" :  ["Death Benefit", "Accidental", "Critical Illness" , "Permanent Disability", "Disaster Relief", "Health Insurance"]}
while(1):
    print("#"*40 + "MENU" + "#"*40)
    print("1.Register new Customer\n2.Add Policy\n3.Registered customers\n4.Available Plans\n5.Add Nominees\n6.Add Benefits\n7.Know your Registered Benefits\n8.Registered Nominees\n9.Annual Premium per Policy\n10.Business Summary\n11.Business Summary per Benefit Group\n12.Business Summary per City\n13.Exit\n")
    print("Choose from the menu")
    choice = int(input())
    if choice == 1:
        idnum = r.randint(100,600)
        print("Customer id generated successfully")
        print(idnum)
        name = input("Enter customer name: ")
        gender = input("Gender: ")
        dob = dt.datetime(*list(map(int,(input("DOB(yyyy mm dd): ").split()))))
        print("Enter address\n")
        hno = input("House number: ")
        city = input("city: ")
        street = input("street: ")
        pincode = input("pincode: ")
        addressObj = Address(hno, city, street, pincode)
        print("Enter contact info\n")
        primemail = input("Primary email: ")
        phno = input("Phone number: ")
        contactObj = Contact(primemail, phno)
        customerObj = Customer(idnum, name, gender, dob, addressObj, contactObj )
        admin.addCustomer(customerObj)
        #print(admin.getCustomer(idnum))
        #print(admin.getAllCustomers())
        print("\n")
    elif choice == 2:
        idnum = int(input("Enter customer ID to add policy to: "))
        pid = r.randint(4000,7000)
        print("Policy ID successfully generated")
        print(pid)
        startdate = dt.datetime(*list(map(int,(input("Start Date(yyyy mm dd): ").split()))))
        matdate = dt.datetime(*list(map(int,(input("Maturity Date(yyyy mm dd): ").split()))))
        riskdate = dt.datetime(*list(map(int,(input("Risk Date(yyyy mm dd): ").split()))))
        term = int(input("Term: "))
        payfreq = int(input("Pay frequency: "))
        policy = Policy(pid, startdate, matdate, riskdate, term, payfreq)
        admin.getCustomer(idnum).addPolicy(policy)
        print("Enter benefit info..\n")
        #bcode = r.randint(10000,20000)
        bgroup = input("Enter Benefit group(Smart Life/Life Security/Nirvana): ")
        #sassured = int(input("Enter sum assured: "))
        #benefit = Benefit(bname, bcode, bgroup, sassured)
        for bname in plans[bgroup.lower()]:
            bcode = r.randint(10000,20000)
            print(bname)
            sassured = int(input("Enter sum assured: "))
            premium = int(input("Premium: "))
            benefit = Benefit(bname, bcode, sassured, premium, bgroup)
            admin.getCustomer(idnum).getPolicy(pid).addBenefit(benefit)
    elif choice == 3:
        print("Registered Customers\n")
        cid = int(input("Enter customer id for retrieval: "))
        cust = admin.getCustomer(cid)
        print(cust.getId())
        print(cust.getName())
        print(cust.getGender())
        print(cust.getDOB())
        print("Policy details: \n")
        for pol in cust.getPolicies():
            print(pol.getId())
            print(pol.getStartDate())
            print(pol.getRiskDate())
            print(pol.getMaturityDate())
            print("------ Benefits ------")
            for ben in pol in pol.getBenefits():
                print(ben.getBenefitCode())
                print(ben.getBenefitName())
                print(ben.getBenefitGroup())
                print(ben.getSumAssured())
                print(ben.getPremium())
                print(" "*10 + "-"*30)
            for nom in pol.getNominees():
                print(nom.getId())
                print(nom.getName())
                print(nom.getRelationship())
                print(nom.getShare())
        '''
        for cust in admin.getAllCustomers():
            print(cust.getId())
            print(cust.getName())
            print(cust.getGender())
            print(cust.getDOB())
            print("-"*50)
        '''
    elif choice == 4:
        print("Available Plans\n")
        for b in admin.getAllPlans():
            print(b)
    elif choice == 5:
        print("Enter Nominee details..\n")
        nid = r.randint(1000,5000)
        print("Nominee ID successfully generated..")
        print(nid)
        name = input("Nominee's name: ")
        rel = input("Relationship with the customer: ")
        share = input("Nominee's share in the benefit: ")
        nominee = Nominee(nid, name, rel, share)
        cid = int(input("Enter customer id: "))
        pid = int(input("Enter policy id: "))
        admin.getCustomer(cid).getPolicy(pid).addNominee(nominee)
    elif choice == 6:
        print("Enter Benefit info..\n")
        bcode = r.randint(10000,20000)
        print("Benefit code generated successfully")
        print(bcode)
        bname = input("Enter Benefit name: ")
        sassured = int(input("Enter sum assured: "))
        premium = int(input("Premium: "))
        benefit = Benefit(bname, bcode, sassured, premium)
        admin.getCustomer(idnum).getPolicy(pid).addBenefit(benefit)
    elif choice == 7:
        cid = int(input("Enter customer ID : "))
        pid = int(input("Enter policy ID : "))
        for ben in admin.getCustomer(cid).getPolicy(pid).getBenefits():
            print()
            print(ben.getBenefitName())
            print(ben.getBenefitCode())
            print(ben.getSumAssured())
            print("-"*40)
    elif choice == 8:
        cid = int(input("Enter customer ID : "))
        pid = int(input("Enter policy ID : "))
        total = 0
        for ben in admin.getCustomer(cid).getPolicy(pid).getBenefits():
            total+=ben.getSumAssured()
            
        for nom in admin.getCustomer(cid).getPolicy(pid).getNominees():
            print()
            print(nom.getId())
            print(nom.getName())
            print(nom.getRelationship())
            print("Share: " + str(nom.getShare()))
            print("Sum Assured Payable: ", end = "")
            print((int(nom.getShare())/100)*total)
            print("-"*40)
    
    elif choice == 9:
        print("Total Annual Premium per policy: ")
        total = 0
        for cust in admin.getAllCustomers():
            for pol in cust.getPolicies():
                total = 0
                print("Policy id: " + str(pol.getId()))
                for ben in pol.getBenefits():
                    total+=int(ben.getPremium()*ben.getPaymentFrequency())
                print("Annual Premium: " + str(total))

    elif choice == 10:
        print("Business Summary: \n")
        ccnt = 0
        pcnt = 0
        bcnt = 0
        tsass = 0
        tpmc = 0
        for cust in admin.getAllCustomers():
            ccnt += 1
            for pol in cust.getPolicies():
                if cust.getStartDate() >= dt.datetime(2018, 4, 1) and cust.getStartDate() <= dt.datetime(2019, 3, 31): 
                    pcnt += 1
                    for ben in pol.getBenefits():
                        bcnt += 1
                        tsass += int(ben.getSumAssured())
                        tpmc += int(ben.getPremium())
        print("No. of customers: " + str(ccnt))
        print("No. of policies: " + str(pcnt))
        print("No. of benefits: " + str(bcnt))
        print("Total Amount Insured: " + str(tsass))
        print("Total Premium Collected: " + str(tpmc))
        
        
    elif choice == 11:
        print("Business Summary per Benefit Group: \n")
        ccnt = 0
        pcnt = 0
        bcnt = 0
        tsass = 0
        tpmc = 0
        sla = 0
        slp = 0
        lsa = 0
        lsp = 0
        nra = 0
        nrp = 0
        for cust in admin.getAllCustomers():
            ccnt += 1
            for pol in cust.getPolicies():
                if cust.getStartDate() >= dt.datetime(2018, 4, 1) and cust.getStartDate() <= dt.datetime(2019, 3, 31): 
                    pcnt += 1
                    for ben in pol.getBenefits():
                        bcnt += 1
                        tsass += int(ben.getSumAssured())
                        tpmc += int(ben.getPremium())
                        if ben.getBenefitGroup().lower() == "smart life":
                            sla += int(ben.getSumAssured())
                            slp += int(ben.getPremium())
                        elif ben.getBenefitGroup().lower() == "life security":
                            lsa += int(ben.getSumAssured())
                            lsp += int(ben.getPremium())
                        else:
                            nra += int(ben.getSumAssured())
                            nrp += int(ben.getPremium())
                            
        print("No. of customers: " + str(ccnt))
        print("No. of policies: " + str(pcnt))
        print("No. of benefits: " + str(bcnt))
        print("Total Amount Insured: " + str(tsass))
        print("Total Premium Collected: " + str(tpmc))

        print("Smart life : ")
        print("Sum Assured : " + str(sla))
        print("Premium Collected : " + str(slp))
        print("Life Security : ")
        print("Sum Assured : " + str(lsa))
        print("Premium Collected : " + str(lsp))
        print("Nirvana : ")
        print("Sum Assured : " + str(nra))
        print("Premium Collected : " + str(nrp))
        
    elif choice == 12:
        print("Business Summary per City")
        hs = set()
        print("Business Summary: \n")
        ccnt = 0
        pcnt = 0
        bcnt = 0
        tsass = 0
        tpmc = 0
        for cust in admin.getAllCustomers():
            
            if cust.getAddress().city not in hs:
                ccnt += 1
            hs.add(cust.getAddress().city)
            for pol in cust.getPolicies():
                if cust.getStartDate() >= dt.datetime(2018, 4, 1) and cust.getStartDate() <= dt.datetime(2019, 3, 31): 
                    pcnt += 1
                    for ben in pol.getBenefits():
                        bcnt += 1
                        tsass += int(ben.getSumAssured())
                        tpmc += int(ben.getPremium())
        print("No. of customers: " + str(ccnt))
        print("No. of policies: " + str(pcnt))
        print("No. of benefits: " + str(bcnt))
        print("Total Amount Insured: " + str(tsass))
        print("Total Premium Collected: " + str(tpmc))
        
        
    elif choice == 13:
        sys.exit()
    else:
        continue
        
        
        
    

        
        
        
