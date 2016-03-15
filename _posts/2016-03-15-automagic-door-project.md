---
layout: post
title: "Automagic Door Project"
date: 2016-03-15 00:43:54
categories:
---
#### Background
I'm living in a dorm! But unfortunately, sometimes my keys get forgotten (through no fault of my own, obviously). They seem to jump right out of my pocket before I leave the room. So I devised a solution.


Back in October, I purchased a Raspberry Pi, a bunch of mini servos, and 25 ft of Ethernet cable. I first attempted to use a continuous servo to activate the handle of my dorm room's door, with limited success. The servo did not have nearly enough torque to consistently pull down the handle. So I bought a stepper motor, 3D printed a mount for it, and attempted to open the door that way. But it still lacked torque. At this point, school began to get harder (and I had mostly stopped forgetting my keys) so I abandoned the project.

#### New Developments
However! A few weeks ago, I was poking around and came across the [Motorola Keylink](http://www.motorola.com/us/consumers/accessories/Motorola-Keylink/keylink.html). It was on clearance, so naturally I picked up 2 of them. As it turns out, they're nearly useless as phone finders when paired with an iPhone; they don't even work when the app isn't active. However, they are essentially little Bluetooth pagers -- you send them a signal from a phone, and they beep. It seemed to me that one would work perfectly for relaying a signal to open a door. Furthermore, it would allow me to avoid the significant headache of connecting the system to the University's local network, and running a secure web server on the Raspberry Pi for activating the door. Taking an entire device out of the mix promised to simplify the project significantly. So I started back at it again, this time planning to only use the stepper, connected to the Keylink and an Arduino. *I'm aware that Bluetooth is probably not completely secure, but the Keylink will not offer to pair with new devices if it's already paired to one, so I figure it's reasonably secure, at least through obscurity.*


#### Gears -- how do they work??
At the same time, I'm trying to learn how to use [Fusion 360](http://www.autodesk.com/products/fusion-360/overview) for CAD, which is a huge step up from the designs that I'd previously been making in SketchUp. However, there's also somewhat of a learning curve, and I'm currently stuck on how to make gears (why are they so complicated?).

![Motor mount in progress](/img/motormount.png)
*The current state of the motor mount*


As soon as I can figure out how gears work, we'll be off to the races! I'm hoping to do so within the next two weeks, since I'll be on break from University.
