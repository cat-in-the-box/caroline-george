print("Answer these questions to see which Democratic presidential primary candidate agrees with you the most on issues of economic inequality.")

'''
Where 2020 Democrats stand on Economic Inequality
(according to the Washington post: https://www.washingtonpost.com/graphics/politics/policy-2020/economic-inequality/)

Questions:
1. Do you support a tax on the assets held by the wealthiest Americans?
2. Should the federal government pay a universal basic income to every American adult?
3. How many weeks should the United States mandate in paid family leave for workers?
4. Should the US government pay reparations to the descendants of slaves?
5. Do you support raising the federal minimum wage to $15 per hour nationwide?
6. Should the federal government guarantee a job to every American?
7. Should the government cancel existing student debt, and if so, for everyone or based on income?
8. Do you support breaking up big tech companies such as Facebook, Google, and Amazon?
9. Do you support raising the federal corporate income tax rate above its current level of 21%?
10. Do you support a national rent control cap?
11. Fed Chairman Jerome Powell has said the current increase in the debt-to-GDP ratio is unsustainable. Would you commit to stabilizing or lowering the debt-to-GDP ratio during your first term?
12. Is the Federal Reserve’s interest rate too high?
13. Would you maintain the standard deduction and child tax credit increases from the Tax Cuts and Jobs Act?
14. Would you consider joining the Comprehensive and Progressive Agreement for Trans-Pacific Partnership?
15. Would you support setting a price on carbon, such as with a carbon tax or cap-and-trade?
'''
#Candidates
Bennet = 0
Biden = 0
Booker = 0
Bullock = 0
Buttigieg = 0
Castro = 0
Delaney = 0
Gabbard = 0
Harris = 0
Klobuchar = 0
Sanders = 0
Sestak = 0
Steyer = 0
Warren = 0
Williamson = 0
Yang = 0

wealthtax = input("\n\n1. Do you support a tax on the assets held by the wealthiest Americans? \n\tA)Hell yeah! \n\tB)No, but let's adjust the capital gains tax. \n\tC)Uhm...IDK. Don't ask me that.\n")
if wealthtax == "a" or wealthtax == "A":
    Buttigieg=Buttigieg+1
    Sanders=Sanders+1
    Steyer=Steyer+1
    Warren=Warren+1
    Williamson=Williamson+1
    print("Buttigieg, Sanders, Steyer, Warren, and Williamson agree with you!")
elif wealthtax == "b" or wealthtax == "B":
    Bennet=Bennet+1
    Biden=Biden+1
    Booker=Booker+1
    Bullock=Bullock+1
    Castro=Castro+1
    Delaney=Delaney+1
    Sestak=Sestak+1
    Yang=Yang+1
    print("Bennet, Biden, Booker, Bullock, Castro, Delaney, Sestak, and Yang agree with you!")
elif wealthtax == "c" or wealthtax == "C":
    Gabbard=Gabbard+1
    Harris=Harris+1
    Klobuchar=Klobuchar+1
    print("Gabbard, Harris, and Klobuchar agree with you!")
else:
    print("I don't understand that input. I am a simple little python program.")

ubi = input("\n2. Should the federal government pay a universal basic income to every American adult? \n\tA)Hell yeah! \n\tB)Hmm...I'm open to it. \n\tC)Hell naw! \n\tD)Uhm...IDK. Don't ask me that.\n")
if ubi == "a" or ubi == "A":
    Gabbard=Gabbard+1
    Williamson=Williamson+1
    Yang=Yang+1
    print("Gabbard, Williamson and Yang agree with you!")
elif ubi == "b" or ubi == "B":
    Castro=Castro+1
    Warren=Warren+1
    print("Castro and Warren agree with you!")
elif ubi == "c":
    Bennet=Bennet+1
    Biden=Biden+1
    Booker=Booker+1
    Bullock=Bullock+1
    Delaney=Delaney+1
    Klobuchar=Klobuchar+1
    Sanders=Sanders+1
    Sestak=Sestak+1
    Steyer=Steyer+1
    print("Bennet, Biden, Booker, Bullock, Delaney, Klobuchar, Sanders, Sestak, and Steyer agree with you!")
elif ubi == "d" or ubi == "D":
    Buttigieg=Buttigieg+1
    Harris=Harris+1
    print("Buttigieg and Harris agree with you!")
else:
    print("I don't understand that input. I am a simple little python program.")

paidleave = input("\n3. How many weeks should the United States mandate in paid family leave for workers? \n\tA)More than 12 weeks \n\tB)12 weeks \n\tC)Fewer than 12 weeks\n")
if paidleave == "a" or paidleave =="A":
    Booker=Booker+1
    Harris=Harris+1
    Sanders=Sanders+1
    Steyer=Steyer+1
    Yang=Yang+1
    print("Booker, Harris, Sanders, Steyer, and Yang agree with you!")
elif paidleave == "b" or paidleave == "B":
    Bennet=Bennet+1
    Biden=Biden+1
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Castro=Castro+1
    Gabbard=Gabbard+1
    Klobuchar=Klobuchar+1
    Sestak=Sestak+1
    Warren=Warren+1
    Williamson=Williamson+1
    print("Bennet, Biden, Bullock, Buttigieg, Castro, Gabbard, Klobuchar, Sestak, Warren, and Williamson agree with you!")
elif paidleave == "c" or paidleave =="C":
    Delaney=Delaney+1
    print("Delaney agrees with you!")
else:
    print("I don't understand that input. I am a simple little python program.")

reparations = input("\n4. Should the US government pay reparations to the descendants of slaves? \n\tA)Hell yeah, I support cash payments. \n\tB)Hmm...Let's study it. I'd supports a commission or other means of determining what form reparations could take. \n\tC)Hell naw, I don't support cash payments.\n")
if reparations == "a" or reparations == "A":
    Williamson=Williamson+1
    print("Williamson agrees with you!")
elif reparations == "b" or reparations == "B":
    Bennet=Bennet+1
    Biden=Biden+1
    Booker=Booker+1
    Buttigieg=Buttigieg+1
    Castro=Castro+1
    Delaney=Delaney+1
    Gabbard=Gabbard+1
    Harris=Harris+1
    Klobuchar=Klobuchar+1
    Sanders=Sanders+1
    Sestak=Sestak+1
    Steyer=Steyer+1
    Warren=Warren+1
    Yang=Yang+1
    print("Bennet, Biden, Booker, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, and Yang agree with you!")
elif reparations == "c" or reparations == "C":
    Bullock=Bullock+1
    print("Bullock agrees with you!")
else:
    print("I don't understand that input. I am a simple little python program.")

minwage = input("\n5. Do you support raising the federal minimum wage to $15 per hour nationwide? \n\tA)Hell yeah! \n\tB)Yes,except in low-cost areas. \n\tC)I have another idea of how to address this issue.\n")
if minwage == "a" or minwage == "A":
    Biden=Biden+1
    Booker=Booker+1
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Castro=Castro+1
    Delaney=Delaney+1
    Gabbard=Gabbard+1
    Harris=Harris+1
    Klobuchar=Klobuchar+1
    Sanders=Sanders+1
    Sestak=Sestak+1
    Steyer=Steyer+1
    Warren=Warren+1
    Williamson=Williamson+1
    print("Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, and Williamson agree with you!")
elif minwage == "b" or minwage == "B":
    Bennet=Bennet+1
    print("Bennet agrees with you!")
elif minwage == "c" or minwage == "C":
    Yang=Yang+1
    print("Yang agrees with you!")
else:
    print("I don't understand that input. I am a simple little python program.")

jobguarantee = input("\n6. Should the federal government guarantee a job to every American? \n\tA)Hell yeah! \n\tB)Hmm...I'm open to it. \n\tC)Hell naw! \n\tD)Uhm...IDK. Don't ask me that.\n")
if jobguarantee == "a" or jobguarantee == "A":
    Sanders=Sanders+1
    print("Sanders agrees with you!")
elif jobguarantee == "b" or jobguarantee == "B":
    Booker=Booker+1
    Harris=Harris+1
    Warren=Warren+1
    print("Booker, Harris, and Warren agree with you!")
elif jobguarantee == "c" or jobguarantee == "C":
    Bennet=Bennet+1
    Biden=Biden+1
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Delaney=Delaney+1
    Gabbard=Gabbard+1
    Klobuchar=Klobuchar+1
    Sestak=Sestak+1
    Steyer=Steyer+1
    Williamson=Williamson+1
    Yang=Yang+1
    print("Bennet, Biden, Bullock, Buttigieg, Delaney, Gabbard, Klobuchar, Sestak, Steyer, Williamson, and Yang agree with you!")
elif jobguarantee == "d" or jobguarantee == "D":
    Castro=Castro+1
    print("Castro agrees with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

studentloan = input("\n7. Should the government cancel existing student debt, and if so, for everyone or based on income? \n\tA)Hell yeah! Cancel all that debt! \n\tB)Cancel student debt based on income. \n\tC)Let's alleviate debt buren some other way. \n")
if studentloan == "a" or studentloan == "A":
    Sanders=Sanders+1
    print("Sanders agrees with you!")
elif studentloan == "b" or studentloan == "B":
    Bennet=Bennet+1
    Booker=Booker+1
    Castro=Castro+1
    Warren=Warren+1
    Williamson=Williamson+1
    print("Bennet, Booker, Castro, Warren, and Williamson agree with you!")
elif studentloan == "c" or studentloan == "C":
    Biden=Biden+1
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Delaney=Delaney+1
    Gabbard=Gabbard+1
    Harris=Harris+1
    Klobuchar=Klobuchar+1
    Sestak=Sestak+1
    Steyer=Steyer+1
    Yang=Yang+1
    print("Biden, Bullock, Buttigieg, Delaney, Gabbard, Harris, Klobuchar, Sestak, Steyer, and Yang agree with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

bigtech = input("\n8. Do you support breaking up big tech companies such as Facebook, Google, and Amazon? \n\tA)Hell yeah! \n\tB)I'm open to it... let's at least strengthen antitrust enforcement.\n")
if bigtech == "a" or bigtech == "A":
    Gabbard=Gabbard+1
    Sanders=Sanders+1
    Warren=Warren+1
    Williamson=Williamson+1
    print("Gabbard, Sanders, Warren, and Williamson agree with you!")
elif bigtech == "b" or bigtech == "B":
    Bennet=Bennet+1
    Biden=Biden+1
    Booker=Booker+1
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Castro=Castro+1
    Delaney=Delaney+1
    Harris=Harris+1
    Klobuchar=Klobuchar+1
    Sestak=Sestak+1
    Steyer=Steyer+1
    Yang=Yang+1
    print("Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Harris, Klobuchar, Sestak, Steyer, and Yang agree with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

incometax = input("\n9. Do you support raising the federal corporate income tax rate above its current level of 21%? \n\tA)Hell yeah! Lets bring it back up to 35%. \n\tB)Yeah, lets bring it up somewhere between 21% and 35%. \n\tC)Yeah. Idk what rate though. \n\tD)I have another idea of how to address this issue \n\tE)Uhm...IDK. Don't ask me that.\n")
if incometax == "a" or incometax == "A":
    Buttigieg=Buttigieg+1
    Castro=Castro+1
    Harris=Harris+1
    Sanders=Sanders+1
    Steyer=Steyer+1
    Warren=Warren+1
    Williamson=Williamson+1
    print("Buttigieg, Castro, Harris, Sanders, Steyer, Warren, and Williamson agree with you!")
elif incometax == "b" or incometax == "B":
    Bennet=Bennet+1
    Biden=Biden+1
    Bullock=Bullock+1
    Delaney=Delaney+1
    Klobuchar=Klobuchar+1
    Sestak=Sestak+1
    print("Bennet, Biden, Bullock, Delaney, Klobuchar, and Sestak agree with you!")
elif incometax == "c" or incometax == "C":
    Booker=Booker+1
    Yang=Yang+1
    Gabbard=Gabbard+1
    print("Booker, Yang, and Gabbard agree with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

rentcontrol = input("\n10. Do you support a national rent control cap? \n\tA)Hell yeah! \n\tB)I have another idea of how to address this issue. \n\tC)Uhm...IDK. Don't ask me that.\n")
if rentcontrol == "a" or rentcontrol == "A":
    Sanders=Sanders+1
    print("Sanders agrees with you!")
elif rentcontrol == "b" or rentcontrol == "B":
    Bennet=Bennet+1
    Biden=Biden+1
    Booker=Booker+1
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Delaney=Delaney+1
    Sestak=Sestak+1
    Steyer=Steyer+1
    Warren=Warren+1
    Williamson=Williamson+1
    Yang=Yang+1
    print("Bennet, Biden, Booker, Bullock, Buttigieg, Delaney, Sestak, Steyer, Warren, Williamson, and Yang agree with you!")
elif rentcontrol == "c" or rentcontrol == "C":
    Castro=Castro+1
    Gabbard=Gabbard+1
    Harris=Harris+1
    Klobuchar=Klobuchar+1
    print("Castro, Gabbard, Harris, and Klobuchar agree with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

debt = input("\n11. Fed Chairman Jerome Powell has said the current increase in the debt-to-GDP ratio is unsustainable. Would you commit to stabilizing or lowering the debt-to-GDP ratio during your first term? \n\tA)Hell yeah! \n\tB)Hell naw! \n\tC)Uhm...IDK. Don't ask me that.\n")
if debt == "a" or debt == "A":
    Bennet=Bennet+1
    Biden=Biden+1
    Delaney=Delaney+1
    Klobuchar=Klobuchar+1
    Steyer=Steyer+1
    print("Bennet, Biden, Delaney, Klobuchar, and Steyer agree with you!")
elif debt == "b" or debt == "B":
    Booker=Booker+1
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Sanders=Sanders+1
    Sestak=Sestak+1
    Warren=Warren+1
    Williamson=Williamson+1
    Yang=Yang+1
    print("Booker, Bullock, Buttigieg, Sanders, Sestak, Warren, Williamson, and Yang agree with you!")
elif debt == "c" or debt == "C":
    Castro=Castro+1
    Gabbard=Gabbard+1
    Harris=Harris+1
    print("Castro, Gabbard, and Harris agree with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

fedreserve = input("\n12. Is the Federal Reserve’s interest rate too high? \n\tA)Hell yeah! \n\tB)Hell naw! \n\tC)The fed should be independent of politics. \n\tD)Uhm...IDK. Don't ask me that.\n")
if fedreserve == "a" or fedreserve == "A":
    Sanders=Sanders+1
    print("Sanders agrees with you!")
elif fedreserve == "b" or fedreserve == "B":
    Sestak=Sestak+1
    Williamson=Williamson+1
    print("Sestak and Williamson agree with you!")
elif fedreserve == "c" or fedreserve == "C":
    Bennet=Bennet+1
    Biden=Biden+1
    Booker=Booker+1
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Delaney=Delaney+1
    Steyer=Steyer+1
    Warren=Warren+1
    Yang=Yang+1
    print("Bennet, Biden, Booker, Bullock, Buttigieg, Delaney, Steyer, Warren, and Yang agree with you!")
elif fedreserve == "d" or fedreserve == "D":
    Castro=Castro+1
    Gabbard=Gabbard+1
    Harris=Harris+1
    Klobuchar=Klobuchar+1
    print("Castro, Gabbard, Harris, and Klobuchar agree with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

taxcutsandjobs = input("\n13. Would you maintain the standard deduction and child tax credit increases from the Tax Cuts and Jobs Act? \n\tA)Hell yeah! \n\tI'd maintain both. \n\tB)I'd maintain the child tax credit. \n\tC)Hell naw! I'd reverse both! \n\tD)Uhm...IDK. Don't ask me that.\n")
if taxcutsandjobs == "a" or taxcutsandjobs == "A":
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Delaney=Delaney+1
    Klobuchar=Klobuchar+1
    Sestak=Sestak+1
    Williamson=Williamson+1
    Yang=Yang+1
    print("Bullock, Buttigieg, Delaney, Klobuchar, Sestak, Williamson, and Yang agree with you!")
elif taxcutsandjobs == "b" or taxcutsandjobs == "B":
    Sanders=Sanders+1
    Steyer=Steyer+1
    Warren=Warren+1
    print("Sanders, Steyer, and Warren agree with you!")
elif taxcutsandjobs == "c" or taxcutsandjobs == "C":
    Bennet=Bennet+1
    print("Bennet agrees with you!")
elif taxcutsandjobs == "d" or taxcutsandjobs == "D":
    Biden=Biden+1
    Booker=Booker+1
    Castro=Castro+1
    Gabbard=Gabbard+1
    Harris=Harris+1
    print("Biden, Booker, Castro, Gabbard, and Harris agree with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

tpp = input("\n14. Would you consider joining the Comprehensive and Progressive Agreement for Trans-Pacific Partnership? \n\tA)Hell naw! \n\tB)I'm open to it... if adjusted. \n\tC)Hell yeah! \n\tD)Uhm...IDK. Don't ask me that.\n")
if tpp == "a" or tpp == "A":
    Booker=Booker+1
    Gabbard=Gabbard+1
    Harris=Harris+1
    Sanders=Sanders+1
    Steyer=Steyer+1
    Warren=Warren+1
    Williamson=Williamson+1
    print("Booker, Gabbard, Harris, Sanders, Steyers, Warren, and Williamson agree with you!")
elif tpp == "b" or tpp == "B":
    Bennet=Bennet+1
    Biden=Biden+1
    Bullock=Bullock+1
    Sestak=Sestak+1
    Yang=Yang+1
    print("Bennet, Biden, Bullock, Sestak, and Yang agree with you!")
elif tpp == "c" or tpp == "B":
    Delaney=Delaney+1
    print("Delaney agrees with you!")
elif tpp == "d" or tpp == "D":
    Buttigieg=Buttigieg+1
    Castro=Castro+1
    Klobuchar=Klobuchar+1
    print("Buttigieg, Castro, and Klobuchar agree with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

carbontax = input("\n15. Would you support setting a price on carbon, such as with a carbon tax or cap-and-trade? \n\tA)Hell yeah! \n\tB)Hmm...I'm open to it. \n\tC)Hell naw!\n")
if carbontax == "a" or carbontax == "A":
    Biden=Biden+1
    Booker=Booker+1
    Bullock=Bullock+1
    Buttigieg=Buttigieg+1
    Castro=Castro+1
    Delaney=Delaney+1
    Harris=Harris+1
    Klobuchar=Klobuchar+1
    Sestak=Sestak+1
    Steyer=Steyer+1
    Williamson=Williamson+1
    Yang=Yang+1
    print("Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Harris, Klobuchar, Sestak, Steyer, Williamson, and Yang agree with you!")
elif carbontax == "b" or carbontax == "B":
    Warren=Warren+1
    Bennet=Bennet+1
    print("Warren and Bennet agree with you!")
elif carbontax == "c" or carbontax == "C":
    Gabbard=Gabbard+1
    Sanders=Sanders+1
    print("Gabbard and Sanders agree with you!")
else: 
    print("I don't understand that input. I am a simple little python program.")

if Bennet >= max(Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print("\n\n\nYou agree most with Bennet on issues of economic inequality.")
if Biden >= max(Bennet, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Biden on issues of economic inequality.")
if Booker >= max(Bennet, Biden, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Booker on issues of economic inequality.")
if Bullock >= max(Bennet, Biden, Booker, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Bullock on issues of economic inequality.")
if Buttigieg >= max(Bennet, Biden, Booker, Bullock, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Buttigieg on issues of economic inequality.")
if Castro >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Castro on issues of economic inequality.")
if Delaney >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Delaney on issues of economic inequality.")    
if Gabbard >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Gabbard on issues of economic inequality.")
if Harris >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Harris on issues of economic inequality.")
if Klobuchar >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Sanders, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Klobuchar on issues of economic inequality.")
if Sanders >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sestak, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Sanders on issues of economic inequality.")
if Sestak >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Steyer, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Sestak on issues of economic inequality.")
if Steyer >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Warren, Williamson, Yang):
    print ("\n\n\nYou agree most with Steyer on issues of economic inequality.") 
if Warren >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Williamson, Yang):
    print ("\n\n\nYou agree most with Warren on issues of economic inequality.")
if Williamson >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Yang):
    print ("\n\n\nYou agree most with Williamson on issues of economic inequality.")
if Yang >= max(Bennet, Biden, Booker, Bullock, Buttigieg, Castro, Delaney, Gabbard, Harris, Klobuchar, Sanders, Sestak, Steyer, Warren, Williamson):
    print ("\n\n\nYou agree most with Yang on issues of economic inequality.")    

print("To find out more about candidate opinions on important issues, visit: https://www.washingtonpost.com/graphics/politics/policy-2020/economic-inequality/.")