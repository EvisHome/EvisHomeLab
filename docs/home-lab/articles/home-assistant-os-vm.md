---
title: Home Assistant OS VM
date: 2022-05-25
description: Running Home Assistant OS as a Proxmox VM.
image: home-assistant-os-vm/thumb.jpg
highlight: false
draft: true
tags:
- home assistant
- Proxmox
- VM
- Self-Hosted
---


# Proxmox | Home Assistant OS

Installing Home Assistant OS on Proxmox VE 7.2-3 as a Virtual Machine, using the
QCOW2 image file and migrating my existing setup.


[IMAGE]


Installing Home Assistant OS on Proxmox VE 7.2-3 as a Virtual Machine and
migrating my previous installation from VMware ESXi.


## Create a VM in Proxmox

Click create VM

### General

* Setting the VM ID (150)
* Set the name (HomeAssistantOS)
* Check start at boot

VM ID is needed later when the image disk is imported and attached to the VM.

[IMAGE]

### OS

[IMAGE]

### System

[IMAGE]

### Disks

[IMAGE]

### CPU

Add the number of CPU cores that you need (I had 6 in ESXi)

[image]

## Memory

## Network

## Confirm

Uncheck Start after created (Do not start the VM), Click Finish. The disk image
needs to be added before the VM is started.