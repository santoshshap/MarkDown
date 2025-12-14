---
status: "Published"
title: "Another test Update Note"
search_terms: "20250723e"
summary: "Summary text from UPN"
access_warning: "True"
release_date: "MM/DD/YYYY"
reissue_date: "MM/DD/YYYY"
published_date: "MM/DD/YYYY"
duration: ""
course_series: ""
membership_level: "Software User"
version_numbers:	
  software version: "25.8.31.544"
  DPR: "25.8.29.167"
  STD: "25.8.27.373"
  GP1: "25.8.10.537"
  GP2: "25.8.10.511"
collect_feedback: "True"
editing_division: ""
editing_department: ""
study_access: ""
study_division: ""
study_department: ""
---
##### **Update Note**

# Another test Update Note

## Forwarding

##### 04 November 2025  

##### (Specific Country)

##### (WiseTech Global Internal only)

##### (Reissue Date)

#####

***

### Summary

This sample Update Note has been created to facilitate GitHub to WTA testing. We will see if this actually works and shows my changes made.
Based on the 'New ALD—Allocated Event added for Consol utilizing Carrier Contract Allocations', it also includes examples of styles and formatting found in the UPN template and other sample files. Images used are for test purposes only. It is not intended to be a facsimile of the original. lets see if these changes will update on my test. Rewrite this summary.
I can't move this.

Why do we have to hit CTRL+ENTER twice?

A new event, 'ALD – Allocated', also supported with Event XML for integration is captured when a Consol is assigned to, modified within, or removed from an Allocation Route of a Carrier Contract. yeah this works fine.  

***

### Table of Contents

[Description](#description)

[ALD - Allocated Event Parameters](#ald---allocated-event-parameters)

[ALD - Allocated Event Reference Field Parameters](#ald---allocated-event-reference-field-parameters)

[Example of a Consol fully allocated to a single Allocation Route](#example-of-a-consol-fully-allocated-to-a-single-allocation-route)

['ALD' Event supports Universal Event XML for System Integration](#ald-event-supports-universal-event-xml-for-system-integration)

***

### Description

To support real-time _integration and enhance traceability_ of allocation usage, a new system event, 'ALD – Allocated', is now captured when a Consol is assigned to, modified within, or removed from a Carrier Contract Allocation Route.

The  'ALD – Allocated' event is recorded on a Consol when the Consol is allocated to an Allocation Route, when allocated values are updated, or when the Consol is unallocated (i.e. removed) from the Allocation Route. Event XML support is included for integration purposes.

We always specialise, authorise, and analyse everything we do. We don't offer judgement, or labour our point. Just humour everyone all the time.

Like other system events, the **'ALD – Allocated'** event can be used to trigger actions such as sending an email notification to the contract manager or transmitting the relevant Event XML to an external system integrated with CargoWise, enabling further processing of allocation data.

The ‘ALD – Allocated’ event is captured on a Consol in the following scenarios:

- When the Consol is allocated to one or more Allocation Routes.
  - When the Consol is removed from one or more Allocation Routes it was previously allocated to.
    - When the Consol, already allocated to Allocation Route(s), has its volume or tonnage updated in a way that changes the utilisation of the associated Allocation Route(s).
    - When the Consol is allocated to one or more Allocation Routes.
  - When the Consol is removed from one or more Allocation Routes it was previously allocated to.
- When the Consol, already allocated to Allocation Route(s), has its volume or tonnage updated in a way that changes the utilisation of the associated Allocation Route(s).

The ‘ALD – Allocated’ event is captured on a Consol in the following scenarios:

1. When the Consol is allocated to one or more Allocation Routes.
    1. When the Consol is removed from one or more Allocation Routes it was previously allocated to.
    1. When the Consol, already allocated to Allocation Route(s), has its volume or tonnage updated in a way that changes the utilisation of the associated Allocation Route(s).
        1. When the Consol is allocated to one or more Allocation Routes.<br>![Test](_images/WI0000STVB-1.png)
        1. When the Consol is removed from one or more Allocation Routes it was previously allocated to.
1. When the Consol, already allocated to Allocation Route(s), has its volume or tonnage updated in a way that changes the utilisation of the associated Allocation Route(s).
Recommended learning: How do I find an Event code for a milestone or trigger?

> [!IMPORTANT]
**Recommended Learning**
>
> - [How do I find an Event code for a milestone or trigger?](https://wisetechacademy.com/search?quickstart=0ac56028-7c3a-4fad-8975-8a3732c6ed34)

The 'ALD – Allocated' event can be viewed on a Consol under the Workflow & Tracking > Events tab:
![image of a Consol under the Workflow & Tracking](_images/WI0000STVB-1.png)
<small>This caption will be small</small>

#### ALD - Allocated Event Parameters

The parameters of the ‘ALD – Allocated’ event are detailed in the table below:

| Parameter | Description |
|----------------|------------------|
| Event Code | ALD |
| Reference | Provides details of the Allocation Route, Carrier Contract, and Carrier utilized by the Consol, along with the allocated quantity, expressed through structured parameters suitable for integration and easy interpretation. <br>**Refer to:** [ALD - Allocated Event Reference Field Parameters](https://wisetechacademy.com/search?quickstart=562a656d-c05c-45e3-8a44-458e88936dab)|
| Event Details | Provides details of the Allocation Route, Carrier Contract and Carrier utilized by the Consol, along with the quantity allocated, expressed in plain language. <br><br>**Examples** <br>Allocated five TEU for Allocation Route AD0000 under Carrier Contract C00001 of Carrier MAELIN_WW. <br>Adjusted allocation to three TEU for Allocation Route AD0000 under Carrier Contract C00001 of Carrier MAELIN_WW. <br>Allocation has been removed and adjusted to zero TEU for Allocation Route AD0000 under Carrier Contract C00001 of Carrier MAELIN_WW.|

> [!IMPORTANT]
**Recommended Learning**
>
> - [Understanding Events and Logs](https://wisetechacademy.com/search?quickstart=20c8bfec-1e90-4d26-95d8-15d561b7b9d0)
> - [How do I use Event Reference Conditions in a Workflow Template?](https://wisetechacademy.com/search?quickstart=03fb6e30-1f03-4c06-8cc7-70556251bf17)

#### ALD - Allocated Event Reference Field Parameters

The parameters used within the Reference field of the 'ALD – Allocated' event are outlined in the table below:

| Types | Description |
|----------------|------------------|
| TYP | The type of unit of the Allocation Route in which the Consol is allocated. <br> 'CNT' is used if the Allocation Route has a Unit of ‘CN’. <br>'TEU' is used if the Allocation Route has a Unit of 'TEU'.|
| QTY | The quantity of containers or TEUs, based on TYP parameter, of the Consol allocated to the Allocation Route. |
| ORG | The Organisation ID of the Service Provider, as specified in the header of the Carrier Contract, in which the Consol is allocated. |
| CON | The Carrier Contract No. of the Carrier Contract in which the Consol is allocated. |
| RFN | The Allocation ID of the Allocation Route in which the Consol is allocated.<br><br>![Test](_images/WI0000STVB-1.png)<br><br>|
| STA | The allocation status between the Consol and the Allocation Route to which it is assigned. <br>'New' is used when the Consol, with all or some of its containers, is allocated to an Allocation Route that has not been previously used by that Consol.<br>'AMD' is used when the Consol is already allocated to an Allocation Route, and the quantity of containers or TEUs allocated has been updated.<br>‘DEL’ is used as when the Consol, previously allocated to an Allocation Route, is now removed from that Allocation Route. |

Individual containers within a Consol can be allocated to different Allocation Routes under the same Carrier Contract. Each Allocation Route used results in one 'ALD – Allocated' event.

Example

If a Consol contains five Containers and they are distributed across three Allocation Routes, only three 'ALD' events will be created, one for each Allocation Route.

> [!Note]
> Support for the 'ALD – Allocated' event in Quick Bookings or Bookings with Quote, when allocating to an Allocation Route, is planned for future CargoWise releases.

##### Example of a Consol fully allocated to a single Allocation Route

An Allocation Route ‘00000007’ is created under the Carrier Contract ‘CCA-2025’ with Service Provider ‘MAELINSYD’:

![The image shows an Allocation Route ‘00000007’ is created under the Carrier Contract ‘CCA-2025’ with Service Provider ‘MAELINSYD’](_images/WI0000STVB-3.png)

##### Example of a Consol fully allocated to a single Allocation Route

An Allocation Route ‘00000007’ is created under the Carrier Contract ‘CCA-2025’ with Service Provider ‘MAELINSYD’:

![The image shows a Consol fully allocated to a single Allocation Route](_images/WI0000STVB-2.png)

#### ‘ALD’ Event supports Universal Event XML for System Integration

Universal Event XML is supported for the 'ALD – Allocated' event, enabling integration with external systems for further processing of allocation data in CargoWise:

The parameters of the 'ALD – Allocated' event are structured as elements within the Universal Event XML, as illustrated below:

```text
<EventType>
<Code>ALD</Code>
<Description>Allocated</Description>
</EventType>
<EventTime>2025-07-02T11:44:59.203+10:00</EventTime>
<EventType>ALD</EventType>
<CreatedTime>2025-07-02T01:44:59.203+00:00</CreatedTime>
<EventReference>|CON=GSS|ORG=US10IMSEA|QTY=1.00|RFN=00000009|STA=NEW|TYP=TEU</EventReference>
Importing a Universal Event XML with 'ALD' as the 'Code' will not currently generate an 'ALD - Allocated' event. Support for this functionality is planned for future CargoWise releases.
```

***
> [!IMPORTANT]
**Recommended Learning**
>
> - [Workflow Templates Reference Guide](https://wisetechacademy.com/search?quickstart=562a656d-c05c-45e3-8a44-458e88936dab)
> - [How are Events automatically logged?](https://wisetechacademy.com/search?quickstart=02ed4920-5570-4fc7-bf4d-e2a1e4465442)
> - [Universal Event XML from Task Events](https://wisetechacademy.com/search?quickstart=7e8a6e8f-7ab8-4173-b2fc-374e68a209a6)

> [!ACTION]
**Support** Press the F1 key from anywhere within CargoWise to raise an eRequest.
>
> 1. Available in CargoWise 25.7.8.116 and later releases.  
> 2. CargoWise Reference: 20250618f / WI00821147, WI00878276, WI00891604, WI00902648, WI00903278, WI00903296, WI00918298, WI00920687, WI00925788, WI00925792, WI00926497, WI00927145, CS01670757, WI00844237, WI00883506, WI00891606, WI00903270, WI00903279, WI00903282, WI00903284, WI00907719, WI00910959, WI00913484, WI00917406, WI00919409, WI00919578, PRJ00051356

These are available Markdown Callouts.

> [!NOTE]
> This is a note.

>
> [!TIP]
> Use this when giving guidance.

>
> [!IMPORTANT]
> This highlights something critical.

>
> [!WARNING]
> Be cautious — this has serious implications.

>
> [!CAUTION]
> Another term for warning.
