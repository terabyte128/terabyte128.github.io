---
layout: page
title: "Patient Fax Tracker"
permalink: /patient_fax_tracker/
hidden: true
---

I worked with a dermatology practice to improve how they manage referrals.

Under certain situations, patient referral information is faxed to the practice, but they cannot enter the patient's information into their electronic medical record system until the patient actually calls in. They had been writing out lists of patients in word-processing software and printing them out every day, which is slow and unwieldy. So I designed a simple web application that allows them to enter patient information as faxes come in:

<a href="/img/faxtracker/add_patient.png"><img style="max-width: 500px;" alt="Entering patient information" src="/img/faxtracker/add_patient.png"></a>

And then view all patients in a fully searchable list, so that when a patient does call in, whoever takes the call can easily find the patient's name and cross-reference it with their ID in the electronic medical record system. The list also auto-updates when patient information is added or removed, ensuring that multiple people can use the app at once without worrying about refreshing the page whenever someone else makes a change.

<a href="/img/faxtracker/full_screen.png"><img style="max-width: 500px;" alt="List view" src="/img/faxtracker/full_screen.png"></a>

Finally, I installed a Raspberry Pi computer in the office to act as a server for the web application. This improves security by keeping all information on their internal network, as opposed to hosting the site somewhere on the Internet.
