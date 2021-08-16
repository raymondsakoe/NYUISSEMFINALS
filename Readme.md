# Final Project - Infant Incubator Model and Simulator

In this assignment you will apply everything you have learned in this module on a real world application, the Infant Incubator. The Infant Incubator is designed to provide a safe, controlled 
space for infants to live while their vital organs develop. Unlike a simple bassinet, an incubator provides an environment that can be adjusted to provide the ideal temperature as well as the perfect amount 
of oxygen, humidity, and light. This paticular Infant Incubator is set to release on **15th August**(Deadline of the Project). The developers of this project would like you, the Security Engineer, to ensure the product satisify US Government's security regulations for medical devices before the release date. As a Security Engineer, you are required **"Make sure we satisfiy US Government Regulations"**. The company has given you the options of accomplishing this by either implementing Vulnerability Patching or creating a Risk Analysis Report.

**Note: You are allowed to do this project individually or with another Security Engineer**

The final deliverables for this project could be either one of these:

## Option 1 - Vulnerability Patching

**Part 1.1 - Identify Vulnerabilities and Testcases**

Your first goal as a Security Engineer who wants to ensure the security of the application is to identify security vulnerabilities in the project and create testcases to exploit them. In the real world, applications are often tested with test scripts. The following are a few questions a Security Engineer would ask when writing a testcase to test the Security of their application:

- "Does this application protect the confidentiaility of data?"
- "Does this application hamper performance?"
- "Does this application prevent actions that shoudl be allowed?"

Notice that these questions are parallel to security paradigms: Security, Efficiency and Accuracy, Availability. If you can find a hypothesis where a security paradigm is not met that would mean the application is not secure and a possible exploit exist. The testcases can be written in python or bash.

Sample Testcase (Will be shared later today):
```
#This is just an example of a testcase
#Vulnerability Name - Authentication available
import socket

def authenticate(p, pw) :
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.sendto(b"AUTH %s" % pw, ("127.0.0.1", p))
    msg, addr = s.recvfrom(1024)
    return msg.strip()

try:
    
    infPort = 23456
    incPort = 23457
    incToken = authenticate(incPort, b"!Q#E%T&U8i6y4r2w")

    # SampleNetworkServer has authentication so the testcase will exit at this assertion.
    assert(incToken != None)
except Exception as ex:
    print (ex)
    assert(1 == 2)

```

**Part 1.2 - Fix the vulnerabilities**

For each of the vulnerabilies you have identified in Part 1.1, fix the vulnerability to ensure they are no longer exploitable.

### **Running the Infant Incubator** 
To run the main code [SampleNetworkServer.py](SampleNetworkServer.py)

```
python3 SampleNetworkServer.py
```

Note: The code only runs on python 3. If you run into the error `ModuleNotFoundError: No Module named 'matplotlib'`, install matplotlib with the following command:
```
pip3 install matplotlib
```

Hint: 
```
#Other ways to connect to the Infant Incubator Server
nc -u 127.0.0.1 23456

#Authenticating with the Server. This should return you a AUTH_TOKEN
AUTH !Q#E%T&U8i6y4r2w

#Running commands with the Server
AUTH_TOKEN;SET_DEGF
or
AUTH_TOKEN;SET_DEGK
```

**What to Submit**

On NYU Brightspace, submit a link to your GitHub repository.

The repository should contain:
 - Testcases (40)
    - Minimum 4 Testcases that works and are real vulnerabilites. (10 for each)
 - Vulnerabilies (40)
    - Minimum 4 Vulnerabilies that works. (10 for each)
    Note: 2 different vulnerability could have the same fix.
 - Vulnerabilies.txt (20)
    - 20 marks for description of the vulnerabilies, testcases and patches.

## Option 2 - Risk Analysis Report
As a Security Engineer, write a detailed Risk Analysis Report for the Infant Incubator application. This report should contain details on the vulnerabilities and how they do not satisify the US Government Regulations(Refer to resources provide below). To identify this vulnerabilies you are encouraged to use tools you have learned in this course such as Threat Modelling and Risk Assesment. In the real world, Security Engineers are not given alot of details about the architecture or details on the program so they often have to make assumptions to find attack vectors and threats. 

Resources:

Software as a Medical Device (SAMD): Clinical Evaluation  Guidance for Industry and  Food and Drug Administration Staff - https://www.fda.gov/media/100714/download

Pre-Market Considerations for Medical Device Cybersecurity - http://www.imdrf.org/docs/imdrf/final/technical/imdrf-tech-200318-pp-mdc-n60.pdf

**What to Submit**

On NYU Brightspace, submit your detailed risk analysis report.

Risk Analysis Report Format:
- Background (Architecture) (20)
- Identify Assets (20)
- Threat Modelling/Risk Analysis (30)
- Apply Security Reviews (How do you mitigate the threats) (30)


## Infant Incubator Model Explained
Cybersecurity education lacks practicality. We know the security principles. We know the importance of cryptography and building-security-in. We know the importance of an adversarial mindset (the security mindset). We know the importance of exposing assumptions (especially implicit ones). However, how many of us know how to apply these theoretical principles in the real world? How to trade off security for the other abilities. While build in security is incomplete, we also need to plan for upgrades.

To appreciate cybersecurity in practice, we must attempt to build a product with cybersecurity in mind. This Infant Incubator is such a product. It will be used as part of the Practical Cybersecurity series of courses that we are developing.

The infant incubator was chosen because:

1. It is a simple, yet valuable product.
2. It is a cyber-physical system that exists in the real world, but can have a virtual (networked) presence.
3. It is a medical device, which means there are laws and regulations that must be accounted for.
4. Safety is paramount, not security. There are no arguments.
5. It can operate as a standalone device, but the allure of being able to control and monitor over the network is there.

## Simple Model

This Infant Incubator Simulator is based on a very simple heat transfer model with three things (or bodies). 

First is the room in which the incubator will sit. We assume that the ROOM is large enough and well controlled so that the temperature never changes over time.

Second is the incubator itself which is modeled as a rectangular prism (box). It has three dimensions, width (w), depth (d) and height (h) all measured in meters. Also this particular incubator is made out of plexi-glass acrylic although other materials can be used as discussed later.

The last body is the infant which is modeled as a body as described in further detail below. 
    
                          ROOM
          ,-----------------------------------.
          |/////   Plexiglass Acrylic   //////|
          |/,-------------------------------./| 
          |/|                               |/|  
          |/|          CHAMBER (HS)         |/| 
        R |/|     ,-------------------.     |/|  R 
        O |/|     |****   SKIN   *****|     |/|  O
        O |/|     |*,---------------.*|     |/|  O
        M |/|     |*|               |*|     |/|  M
          |/|     |*|  INFANT (HS)  |*|     |/|
          |/|_____|*|_______________|*|_____|/|
    
                        INSULATOR
    

As shown, this is a closed system where 5 of the 6 faces of the incubator are exposed to the room; the bottom face is not. Imagine the incubator being placed on an insulating pad where heat loss is negligible.

Since the infant is normally placed in the middle of the incubator bed, we assume that there is no direct contact between skin and the chamber walls. As a result, all energy transfers are either between the Incubator Chamber and the Room through the Plexiglass or, in the case when an infant is inside, between the Infant and the Incubator through skin. 

## Energy/Heat Transfer Calculations

The law of thermodynamics that energy must be conserved. Any energy lost (or gained) by the Chamber must be gained (or lost) by the Infant or the Room. To simplify things further, we will also assume that energy is always uniformly distributed within each body which means that the temperature is also uniform. With this assumption, we can always calculate the current temperature of a thing given its energy content or the energy content given its temperature as long as we know its specific heat.

Specific heat is not constant. It changes with temperature and pressure, but we will not account for this in this model. For simplicity, we use the following values.

- The specific heat for Air at sea level (1 ATM) is 1.012 J / g / degK = 1012 J / kg / degK
- The specific heat for Animal Tissue is about 3.5 J / g / degK.       = 3500 J / kg / degK

To calculate the mass of air (in Chamber ) or the Infant we also need to know the density and volume. However, while volume makes sense for the chamber -- width (or lenght), depth, height -- Infants are normally measured with their weight and length. We know that weight depends on gravity, which in turn varies by location, but will also conveniently ignore that and assume that weight and mass are equal. As mentioned above, we will also ignore the size of the room by assuming that the temperature in the room is always constant (meaning there is some external heat source or sink that ensures this). 

Once again the densities can change given environmental and other conditions, but we will use the following constants.

- The density of a human body is about the same as that of water   = 1000 kg/m^3.
- The density of air at room temperature (20 degC and 101.325 kPa) = 1.2041 kg/m^3)

Given the constants above and initial state information, the total energy that is latent in the two systems (Chamber and Infant) can be calculated. 

### Heat Transfer

Heat transfer does not take place instantaneously but at a specifed rate. The rate at which heat (energy) is transferred varies depending on environmental conditions but also on how the transfer occurs (conduction, convection or radiation.) For convenience reasons, we will assume that heat transfer can be modeled using a single constant U (known as the U-factor). We use the following values:

- Heat transfer through human skin occurs at a rate of 5.5 W / m^2 / degK ([2]) = 5.5 J / S / m^2 / degK
- Heat transfer through plexiglass at a rate of .90 BTU/hr/SqFt/degF            = 5.11 J / S / m^2 / degK

Since the degK is the degrees of temperature difference between the two sides of the material, this means that we need to know what the temperature of the Infant, Chamber and Room are in order to use calcuate the amount of energy transfer. Then after the energy has been transfered over a specific period of time, we will need to update the temperature accordingly for the next iteration of the simulation.

The reliance on temperature differential is convenient since we think of Infants and chambers having a temperature of X rather than an energy of X.

In addition to the temperature differential, the heat transfer constants also depend on the exposed surface area. The surface area for the Chamber is wd (for top) + 2wh (front and back) + 2dh (sides). The surface area of a human body is more complicated, although there is a number of formulas that approximate surface area. One of them is the Mosteller formula which is SQRT(mass * length / 3600). In this case, mass is in kg but length is in cm which means surface area of a human body is SQRT(100 * m * l / 3600) where the resulting unit is m^2, kg for mass and m for height. We do not account for the fact that most parts of the infant will not be exposed to air. 

## Simulation

Putting everything together, the simulation will take place in a sequence of coordinated steps. 

During each timestep (simulation iteration) we will:

1. Calculate temperature differentials T\_RC and T\_CI for the difference in temperatures between the Room and Chamber and Chamber and Infant respectively.
2. Calculate E\_I, the energy gained by the Infant's internal heater, i.e. energy gained due to metabolism over the past timestep.
3. Calculate E\_IC, the energy gained (or lost if negative) by the Infant, using T\_CI and the constants above. This is the same amount of energy that will be lost (or gained) by the Chamber due to the Infant.
4. Calculate E\_C, the energy gained by the Chamber's heater. 
5. Calculate E\_CR, the energy gained (or lost if negative) by the Chamber to the Room using T\_RC and the constants above.
6. Update the energy content and temperature of the Infant and Chamber using E\_I, E\_IC and E\_CR. We do not update Room since it is assumed to maintain the same temperature.

Second is the infant which is also modeled as a box of sorts. The infant will have a defined weight with which the volume will be calculated. This volume will displace air in the incubator as expected. Furthermore, we will assume that the surface area is known as a constant as well as the heat source within the infant (metabolism) which is once again assumed to be instantaneous and uniform. 

### Threading

The simulator is multithreaded. The Chamber, Room and Infant will all run within a single thread because they are tightly coupled (see equations above). Since the heat source (due to metabolism) for the Infant is part of the Infant, it will also run within the main simulator thread. All of the other components will run as separate threads. The heater for the chamber, the thermometer used to measure the temperature of the infant and the thermometer used to measure the temperature of the chamber run in their own separate threads. In this way, as more features are added, more advanced problems such as real-time constraints, race-conditions, and faults will naturally surface.

## Additional Notes:

### Chamber Operations

Since chambers aren't necessarily turned on all of the time, one would expect that the incubator will be empty and at room temperature to begin with. The heater will be turned on to warm it up to a desired temperature and then the infant will be placed inside it when the target temperature has been reached. However, it is also expected that the process of opening the chamber will result in heat loss since it is now mixing with the air in the room. We chose to implement these conditions as two special events.

1. When the chamber is open, we will assume that it will result in a change in temperature that is proportional to the difference in temperatures between the room and the chamber. In other words NewChamberTemp = C x (OldChamberTemp - RoomTemp)
2. When an infant is placed into the chamber, we will simply note the current temperature of the chamber, reduce the volume of air by the volume of the infant and then update the energy content accordingly.
3. When an infant is removed from the chamber, we will simply replace the infant with the same volume of air at the same temperature as the chamber. A better approach is to replace it with room temperature air.

### Heat Transfer Constant for Plexiglass

The value of .90 was obtained from the table of U-Factors in [5]. It is the constant for plexiglass with "Summer Conditions" and a thickness of 6.0mm or 1/4" installed vertically.

For some quick conversions: 
1 BTU/hr = .293071 W  => .293071 W / BTU/hr
1 SqFt = .092903 m^2 => .092903 m^2 / ft^2
1 deltaF = 5/9 deltaK => 5/9 degK / degF

This means that the U-Factor of .90 (BTU/Hr) / ft^2 / degF = .90 x .293071 / .092903 / (5/9) = 5.11 W / m^2 / degK.

Note that there is also a different datasheet for PERSPEX and glass windows measured in W/m^2 / degC which at 5mm (single pane) is 5.5 for glass and 4.9 for PERSPEX acrylic [6]. The numbers seem close enough so it is a nice double check.


## Bibliography:

1. [https://ergo.human.cornell.edu/studentdownloads/DEA3500notes/Thermal/thcondnotes.html]
2. [https://bioheat.umbc.edu/files/2015/07/JTB2016_ForensicScience.pdf]
3. [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4319855/]
4. [https://www.jidonline.org/article/S0022-202X(15)45119-X/pdf]
5. [https://www.acrylite.co/technology-center/u-factors/]
6. [https://www.allplastics.com.au/component/docman/doc_download/93-allplastics-perspex-datasheet-for-glazing-pdf?Itemid=]
7. [https://www.nursingcenter.com/ncblog/august-2017/body-mass-index-and-body-surface-area-what-s-the-d]

## Special Acknowledgements

We would like to thank Prof. John Hatcliff of Kansas State University and Mr. Todd Carpenter of Adventium Labs Dr. Raj Rajagopalan of Resideo for their invaluable insights and help in developing the Practical Cybersecurity concept as well as the Infant Incubator project.

# LICENSE

Copyright 2021 Lok Yan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
