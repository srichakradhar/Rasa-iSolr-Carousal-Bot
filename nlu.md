
## intent:check_balance
- what is my balance <!-- no entity -->
- how much do I have on my [savings](source_account) <!-- entity "source_account" has value "savings" -->
- how much do I have on my [savings account](source_account:savings) <!-- synonyms, method 1-->
- Could I pay in [yen](currency)?  <!-- entity matched by lookup table -->

## intent:greet
- hi there
- hello there
- hey
- hi
- hey bot
- hello

## intent:wish
- good morning
- goodmorning
- goodevening
- goodafternoon
- good evening
- morning
- good afternoon

## intent:thankyou
- um thank you good bye
- okay cool uh good bye thank you
- okay thank you good bye
- you rock
- adios
- goodbye
- good bye
- bye bye
- bye
- and thats all thank you and good bye
- thank you and good bye
- sorry about my mistakes thank you good bye
- noise thank you good bye
- thank you goodbye noise
- okay thank you goodbye
- uh thank you good bye
- thank you goodbye
- thank you goodbye noise thank you goodbye
- breath thank you goodbye
- thank you
- okay thank you
- thanks goodbye
- ah thank you goodbye
- thank you noise
- thank you good bye
- breath thank you very much goodbye
- thanks
- noise thank you goodbye
- unintelligible thank you goodbye
- uh okay thank you good bye
- thank you bye
- um okay thank you good bye

<!-- ## intent:release
- IOS XE Gibraltar [16.10.x](version)
- IOS XE Gibraltar [16.6.1](version) -->

## intent:query
- Can you give me an example of sample campus fabric topology in cat [9300](series)?
- how does IP Address get assigned to DHCP Client?
- How does packet flow happen in DHCP solution?
- How many access points can be connected to the fabric?
- Can you give me an example of sample campus fabric topology in cat [9300](series)?
- How does packet flow happen in DHCP solution
- How many access points can be connected to the fabric
- how to configure your device as a fabric border device
- How do I take a port out of error-disabled state?
- What is the Default MSTP Configuration for Cat [9300](series)?
- Which commands are used to monitor GIR in Cat [9300](series)?
- Why is notes field for telemetry ietf subscription command in cat [9300](series) always empty?
- What command should I run on Cat [9300](series) to check basic network connectivity?
- How should I configure  the EEM Python Policy on Catalyst [9300](series)?
- What is Zero-touch provisioning on Cat [9300](series) switches?
- Can I automate management of Cisco Catalyst [9300](series)?
- What are the variables for the install command on Cat [9300](series)?
- How do I configure iox services on Catalyst [9300](series)?
- What is the difference between ping and ping4 commands on Cat [9300](series)?
- How do I view the status of an installed model package update on cat [9300](series)?
- I need information about the Cisco Python Module for Cat [9300](series)
- What Python version is supported on Cat [9300](series)?
- How does iPXE boot loader work on Catalyst [9300](series)?
- how to configure hsrp on Catalyst [9300](series)
- how to configure sdm template on [9300](series)
- What is the command to enable a system image boot on Cat [9300](series)?
- What are the pre-reqs for a model-driven telemetry on Cat [9300](series)?
- Does the switch Cisco Catalyst 9300 support IoT ?
- Does the switch Cisco Catalyst 9300 support Mobility ?
- Is Cloud supported on the switch Catalyst [9300](series) ?
- On which platform Cisco Catalyst [9300](series) series switch will run ?
- Does Catalyst 9300 have the capacity to host containers ?
- Which OS does Cisco Catalyst [9300](series) run ?

## regex:series
- [0-9]{4}

## lookup:currencies   <!-- lookup table list -->
- Yen
- USD
- Euro
<!--
## lookup:additional_currencies  <!-- no list to specify lookup table file -->
<!-- path/to/currencies.txt -->

## synonym:9300
- 9300 series switch
- cisco 9300
- cat 9300
- catalyst 9300

## synonym:16.6.1
- Everest 16.6.1
- Zealand
- Fuji 16.9.x