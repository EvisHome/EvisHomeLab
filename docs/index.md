---
title: Home
date: 2025-12-20
description: explore the EvisHomeLab documentation covering Smart Home automation, Server Infrastructure, and Networking topologies.
hide:
  - navigation
  - toc
render_macros: true
---

<style>
  /* Hide title and edit button */
  .md-typeset h1, .md-content__button {
    display: none;
  }
  /* Remove default top padding/margins for ALL main content containers */
  .md-container, .md-content, .md-content__inner, .md-main__inner, .md-main {
    padding-top: 0 !important;
    margin-top: 0 !important;
  }
  /* CRITICAL FIX: Hide the pseudo-element that adds 0.4rem top spacing */
  .md-content__inner::before {
    display: none !important;
    content: none !important;
  }
  
  /* ROBUST CROSS-BROWSER FIX: Kill ghost spacing from line-height/font-size */
  .hero-section {
    margin-top: 0 !important;
    padding-top: 0 !important;
    line-height: 0 !important;
    font-size: 0 !important;
  }
  
  .hero-section video, .hero-section a {
    display: block !important;
    margin: 0 !important;
    padding: 0 !important;
    vertical-align: top !important;
  }
</style>




<div class="hero-section">
    <div class="hero-inner" style="position: relative; width: 100%; max-width: 1200px; margin: 0 auto;">
        {# {{ hero_overlay("Virtual Fireplace", "Featured Project", "articles/virtual-fireplace/") }} #}
        <video autoplay loop muted playsinline style="cursor: default;">
            <source src="assets/images/intro-1080-2000.mp4" type="video/mp4">
        </video>
    </div>
</div>


<div class="content-grid">
    <a href="articles/" class="content-card">
        <h3>Articles</h3>
        <p>Collection of articles and guides.</p>
    </a>
    <a href="home-lab/" class="content-card">
        <h3>Home Lab</h3>
        <p>Networking, Server Infrastructure, VMs, and containers.</p>
    </a>
    <a href="smart-home/" class="content-card">
        <h3>Smart Home</h3>
        <p>Home Assistant configuration, automations, and dashboards.</p>
    </a>
    <a href="tags/" class="content-card">
        <h3>Tags</h3>
        <p>Browse the content by tags.</p>
    </a>
</div>

## Featured
<div class="feature-grid">
    <a href="workflow/" class="feature-card">
        <span>Documentation</span>
        <h4>Architecture & Workflow</h4>
        <p>See how the Home Assistant documentation is managed via an Agentic Documentation Workflow.</p>
    </a>
    <a href="smart-home/dashboards/" class="feature-card">
        <span>Home Assistant</span>
        <h4>Dashboards</h4>
        <p>Check the dashboards for the Home Assistant</p>
    </a>
    <a href="smart-home/packages" class="feature-card">
        <span>Home Assistant</span>
        <h4>Automations</h4>
        <p>Deep dive into the Home Assistant automations and dashboards.</p>
    </a>
</div>

## The Lab

<div class="media-grid">
    <a href="articles/articles/the-rack/light-preview.jpeg" class="glightbox">
        <img src="articles/articles/the-rack/light-preview.jpeg" alt="Rack Lights">
    </a>
    <a href="articles/articles/the-rack/the-rack.mp4" class="glightbox" data-width="100%" data-height="auto">
        <video width="100%" autoplay loop muted playsinline style="cursor: pointer;">
            <source src="articles/articles/the-rack/the-rack.mp4" type="video/mp4">
        </video>
    </a>
    <a href="articles/articles/the-rack/lab-preview.jpeg" class="glightbox">
        <img src="articles/articles/the-rack/lab-preview.jpeg" alt="Lab Lights">
    </a>
    <a href="articles/articles/the-rack/rack-back.jpeg" class="glightbox">
        <img src="articles/articles/the-rack/rack-back.jpeg" alt="Rack Back">
    </a>
    <a href="articles/articles/the-rack/rack-front.png" class="glightbox">
        <img src="articles/articles/the-rack/rack-front.png" alt="Rack Front">
    </a>
    <a href="articles/articles/the-rack/rack-door.jpeg" class="glightbox">
        <img src="articles/articles/the-rack/rack-door.jpeg" alt="Rack Closed">
    </a>
</div>

## About Me

I've had a passion for home automation, DIY, self-hosting for a while now. I'm a big fan of Home Assistant and have been using it for since 2019-2020. I have documented my journey on various platforms, but I've always wanted to have a single place to keep everything in one place. Now with the help of Google Antigravity and the MkDocs Material theme, I've been able to create a single place to keep everything in one place. And the speed of creating everything into this site has been just amazing. Withing just few weekends I was able to create this site automate the documentation process convert some of my older articles and make them into markdown files and add them to the site.

My Smart Home journey started along time ago I think somewhere around 2005with having too many remote controllers for my home theater system. I started with a basic setup using a Raspberry Pi and a few scripts to control the system. Over time, I added more and more features, such as voice control, scene management, and more.

Before I moved to Home Assistant I used SmartThings with Webcore, SmartApps and Device Handlers (DTHs), which ran in the Groovy IDE. For some years I was using this setup, with a lot of custom code and a lot of time spent on debugging and just maintaining the system.

Ever since I fully moved to Home Assistant things have been much easier and I've been able to focus on actual home automation, and making things smarter.

