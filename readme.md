<p align=center>
  <img src="assets/haicon.png"/>
  <h1 align=center>Home Automation</h1>
  <p align=center>A simple starting point to Home Automation inside a universitary apartement room.</p>
</p>
<h1></h1>
<p align=center>
  <a href="https://travis-ci.org/eliseomartelli/HomeAutomation-Config">
    <img src="https://travis-ci.org/eliseomartelli/HomeAutomation-Config.svg?branch=master"/>
  </a>
  <a href="https://github.com/eliseomartelli/HomeAutomation-Config/tree/master">
    <img src="https://img.shields.io/badge/Branch-master-green.svg?longCache=true"
        alt="Branch">
  </a>
  <img alt="undefined" src="https://img.shields.io/github/last-commit/eliseomartelli/HomeAutomation-Config.svg">
  <img alt="undefined" src="https://img.shields.io/github/license/eliseomartelli/HomeAutomation-Config.svg">
  <img src="https://img.shields.io/badge/haversion-0.86.4-blue.svg">
</p>

## What's in my room?
### Switches
| # | Type | Protocol |
|---|---|---|
| 3 | Plugs | 433MHz* |
| 1 | Lamp Socket | 315MHz* |
| 1 | RGB Light Strip | MQTT |

### Sensors
| # | Type | Protocol |
|---|---|---|
| 1 | Motion | MQTT |
| 1 | Temperature | DHT One Wire* |
| 1 | Humidity | DHT One Wire* |

### Cameras 
| # | Type | Protocol |
|---|---|---|
| 1 | PS3 Eye Camera | USB |

### Misc
| # | Type | Protocol |
|---|---|---|
| 1 | Tablet | |
| 1 | Epson XP-205 Printer | Network |
| 1 | Amazon Dash Button | Network |
| 1 | Google Home Mini | Network | 
| 1 | RPI Zero W | Network | 

## Made By Me (DIY)
- RGB Light Controller (ESP8266 based)
- RF Bridge (Raspberry Pi Zero W)
- Security Camera Bridge (Raspberry Pi Zero W)(MotionEye)

## What I Run?
- 2 instances of Home Assistant (3 including the development one)
- 1 instance of AppDaemon
- 1 instance of MotionEye
- 1 instance of AmazonDash

## In the cloud ☁
- 1 instance of "Cute Cat" CloudMQTT (Owntracks)

* (Bridged to MQTT with the second instance of HA)

## Screenshots 
![](assets/ha1-min.png)
![](assets/ha2-min.png)
![](assets/ha3-min.png)
![](assets/ha4-min.png)
![](assets/ha5-min.png)

### HaDashboard  

![](assets/hadashboard-min.png)
