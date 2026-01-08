# Motorized Horizontal Blinds - Tilt Action

## Overview

Motorizing and automating horizontal window blinds tilt with a stepper motor and ESP board using ESPHome, to be controlled from Home Assistant, NodeRED, and with Philips Hue Dimmer switches. 3D printed parts are needed to at least mount the motor to the blinds, additionally, you can print enclosures for the parts.


<video controls autoplay muted>
  <source src=" ../motorized-blinds/motorized-blinds-demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Parts

* ESP8266 (D1 Mini, or NodeMCU)
* Stepper driver A4899 or DRV8825 (Note: pin layouts are slightly different)
* 28BYJ-45 stepper motor (5V) - converted to bipolar stepper
* MP1584EN Buck Converter
* 12V Power Supply
* 3D Printed parts: enclosure for the ESP and buck converter, adapter to attach the blind's axel to the motor. Mounting to attach the motor to the window frame and enclosure for the stepper driver.
* For wiring, I used an old cat6 ethernet cable

![Parts](../motorized-blinds/parts.jpg)

## Build

Before wiring everything up, the 28BYJ - 48 - Stepper Motor needs to be converted to bipolar

### Converting 28BYJ Stepper Motor to Bipolar

The 28BYJ is a 5-wire unipolar stepper motor and it comes with a ULN2003 driver. To get the most torque out of this motor, you can momentarily supply more voltage for it than designed, without burning it. But to use more than the 5V, a different driver than the ULN2003 is needed.

To use the DRV8825 or A4988, the motor needs to be converted to a bipolar motor. To convert the 28BYJ to bipolar you only need to cut the common voltage connection between the coils.

To do so carefully remove the blue cover from the motor and just scrape (cut) the center trace with a small screwdriver. 

![28BYJ to Bipolar](../motorized-blinds/28BYJ-to-bipolar.png)

### Wiring Diagrams

Wiring for DRV8825 Stepper Driver
![With DRV8825 Stepper Driver](../motorized-blinds/image-16.png)

Wiring for A4988 Stepper Driver
![With A4988 Stepper Driver](../motorized-blinds/image-17.png)

Example of using two motors with two DRV8825 drivers
![Two motors](  ../motorized-blinds/image-44.png)


### ESPHome Code

```yaml
--8<-- "docs/home-lab/articles/motorized-blinds/esphome.yaml"
```

## 3D Printed Parts

* [Motor Mount and the Adapter](https://www.tinkercad.com/things/lNaTwFwwbym-horizontal-blinds-adapter)
* [Motor Driver Enclosure](https://www.tinkercad.com/things/39l2595FxH0-horizontal-blinds-motor-driver)
* [D1 Mini Enclosure](https://www.tinkercad.com/things/inkHXLinVQN-wemos-d1-mini-case)
* [NodeMCU Enclosure](https://www.tinkercad.com/things/aECL7EiqNli-nodemcu-buck-converter-case)


